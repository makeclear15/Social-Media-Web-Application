from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from .models import Users, Profiles, Posts
from .models import *
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request, 'index_new.html')


def sample(request):
    return render(request, 'sample.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def admin(request):
    usr = Users.objects.all()
    prof = Profiles.objects.all()
    return render(request, 'admin.html', {'Users': usr, 'Profiles': prof})

def user_nav(request):
    return render(request,'user/user_nav_bar.html')


def user_post(request,user_id):
    uid = Users.objects.get(user_id=user_id)
    followings = Following.objects.filter(user_name=uid.username)
    # Retrieve usernames not in the 'following' queryset
    suggestions = Users.objects.exclude(
        username__in=followings.values_list('following', flat=True)
    ).exclude(user_id=user_id)[:5]
    if Following.objects.filter(user_name=uid.username).exists():
        following_ids = [following.following_id for following in followings]
        posts = Posts.objects.filter(user_id__in=following_ids).order_by('-post_id')
        return render(request,'user/user_post.html',{'Posts': posts,'user': uid,'follow':suggestions})
    return render(request,'user/user_post.html',{'user': uid,'follow':suggestions})

@login_required(login_url='Home')
def user_post_new(request,user_id):
    uid = Users.objects.get(user_id=user_id)
    if Profiles.objects.filter(user_id=user_id).exists():
        prof = Profiles.objects.get(user_id=user_id)
        return render(request,'user/user_post_new.html',{'user': uid,'Profiles': prof})

    return render(request,'user/user_post_new.html',{'user': uid})

@login_required(login_url='Home')
def user_post_sample(request, user_id):

    uid = Users.objects.get(user_id=user_id)
    followings = Following.objects.filter(user_name=uid.username)
    # Retrieve usernames not in the 'following' queryset
    suggestions = Users.objects.exclude(
        username__in=followings.values_list('following', flat=True)
    ).exclude(user_id=user_id)[:5]

    # if Profiles.objects.filter(user_id=user_id).exists():
    prof = Profiles.objects.get(user_id=user_id)

    uid1 = Users.objects.filter(user_id=user_id)
    if Following.objects.filter(user_name=uid.username).exists():
        following_ids = [following.following_id for following in followings]
        posts = Posts.objects.filter(user_id__in=following_ids).order_by('-post_id')

        data = {
            'Posts': list(posts.values()),
            'user': list(uid1.values()),  # User data
            'follow': list(suggestions.values()),  # Suggestions data
            # 'prof': list(prof.values())
        }

        return JsonResponse(data)

    # If the user is not following anyone
    data = {
        'user': list(uid1.values()),  # User data
        'follow': list(suggestions.values())
        # Suggestions data
    }

    return JsonResponse(data)

def get_post(request, user_id):
    posts_old = Posts.objects.exclude(user_id=user_id).order_by('-post_id')
    posts = list(posts_old.values())
    return JsonResponse(posts, safe=False)

# Add Post
@login_required(login_url='adminsignup')
def add_post_view(request,user_id):
    uid = Users.objects.get(user_id=user_id)
    return render(request,'user/add_post.html',{'user':uid})

@login_required(login_url='Home')
def add_post(request, user_id):
    if request.POST:
        user_id = user_id
        uid = Users.objects.get(user_id=user_id)
        user_name = uid.username
        content = request.POST['postDescription']
        post_title = request.POST['postTitle']
        media_type = request.POST['media_type']
        # media_type = 'Image'
        media_url = request.FILES['postFile_url']
        profile_picture_url = Profiles.objects.filter(user_id=user_id).values('profile_picture_url')
        print(profile_picture_url)

        post = Posts(user_id=user_id, content=content, media_type=media_type, media_url=media_url,
                     post_title=post_title, user_name=user_name,profile_picture_url=profile_picture_url)
        post.save()
        prof = Profiles.objects.get(user_id=user_id)
        prof.no_of_posts = prof.no_of_posts+1
        prof.save()
        return redirect(reverse('user_post_new',args=[user_id]))
    else:
        return redirect(reverse('user_post_new',args=[user_id]))
@login_required(login_url='Home')
def manage_post(request, user_id):
    uid = Users.objects.get(user_id=user_id)
    posts = Posts.objects.filter(user_id=user_id).order_by('-post_id')
    return render(request, 'user/manage_post.html', {'Posts': posts, 'user': uid})
@login_required(login_url='Home')
def edit_profile(request,user_id):
    uid = Users.objects.get(user_id=user_id)
    if Profiles.objects.filter(user_id=user_id).exists():
        prof = Profiles.objects.get(user_id=user_id)
        if Posts.objects.filter(user_id=user_id).exists():
            posts = Posts.objects.filter(user_id=user_id).order_by('-post_id')
            return render(request, 'user/user_profile.html', {'user': uid, 'Profiles': prof, 'Posts': posts})
        return render(request, 'user/user_profile.html', {'user': uid, 'Profiles': prof})
    return render(request,'user/user_profile.html',{'user': uid})

@login_required(login_url='Home')
def following(request):
    user_name = request.user.username
    try:
        following = Following.objects.filter(user_name=user_name)
        following_list = list(following.values())  # Convert queryset to list of dictionaries
        following_ids = following.values_list('following_id', flat=True)
        following_urls = Profiles.objects.filter(user_id__in=following_ids).values('user_id', 'profile_picture_url')
        following_urlss = list(following_urls)
        response = {
            'following': following_list,  # Return the list of following
            'following_urls': following_urlss  # Return the list of following
        }
        return JsonResponse(response)
    except Following.DoesNotExist:
        return JsonResponse({'message': 'No following found for user {}'.format(user_name)}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@login_required(login_url='Home')
def followers(request):
    user_name = request.user.username
    try:
        following = Following.objects.filter(following=user_name)
        following_list = list(following.values())
        following_ids = following.values_list('following_id', flat=True)
        following_urls = Profiles.objects.filter(user_id__in=following_ids).values('user_id', 'profile_picture_url')
        following_urlss = list(following_urls)
        response = {
            'followers': following_list,  # Return the list of following
            'following_urls': following_urlss  # Return the list of following
        }
        return JsonResponse(response)
    except Following.DoesNotExist:
        return JsonResponse({'message': 'No following found for user {}'.format(user_name)}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@login_required(login_url='Home')
def search_profile(request):
    return render(request,'user/search_profile.html')

@login_required(login_url='Home')
def search_profiles(request,user_name):
    if Users.objects.filter(username__istartswith=user_name).exists():
        user = Users.objects.filter(username__istartswith=user_name)
        username = request.user.username
        uid = Users.objects.get(username=username)
        usr_ids = user.values_list('user_id',flat=True)
        prof = Profiles.objects.filter(user_id__in=usr_ids)
        follow = Following.objects.filter(user_name=uid.username)
        follows = [item.following for item in follow]
        return render(request,'user/search_profile.html',{'Profiles':prof,'Users':user,'user': uid,'follows':follows})
    return render(request,'user/search_profile.html')

def like_post(request):
    post_id = request.GET.get('post_id')
    username = request.user.username
    uid = Users.objects.get(username=username)
    user_id = uid.user_id

    post = Posts.objects.get(post_id=post_id)

    like_filter = Likes.objects.filter(post_id=post_id,username=username).first()

    if like_filter == None:
        new_like = Likes.objects.create(post_id=post_id,username=username)
        new_like.save()
        post.likes_count = post.likes_count+1
        post.save()
        # return redirect('')
        return redirect(reverse('user_post', args=[user_id]))
    else:
        like_filter.delete()
        post.likes_count = post.likes_count-1
        post.save()
        return redirect(reverse('user_post', args=[user_id]))

def add_comment(request):
        post_id = request.GET.get('post_id')
        content = request.GET.get('comment_text')
        username = request.user.username
        uid = Users.objects.get(username=username)
        user_id = uid.user_id

        post = Posts.objects.get(post_id=post_id)

        new_comment = Comments.objects.create(
            post_id=post_id,
            content=content,
            comment_date=timezone.now(),
            username=username
        )
        new_comment.save()
        post.comments_count = post.comments_count + 1
        post.save()
        message = "Comment Saved"

        return JsonResponse({'message': message})

def get_comment(request):
    post_id = request.GET.get('post_id')

    comments1 = Comments.objects.filter(post_id=post_id).order_by('-comment_id')
    comments = list(comments1.values())

    data = {
        'comments': comments
    }

    return JsonResponse(data)

@login_required(login_url='Home')
def like_post_new(request):
    post_id = request.GET.get('post_id')
    username = request.user.username
    uid = Users.objects.get(username=username)
    user_id = uid.user_id

    post = Posts.objects.get(post_id=post_id)

    like_filter = Likes.objects.filter(post_id=post_id,username=username).first()

    if like_filter == None:
        new_like = Likes.objects.create(post_id=post_id,username=username)
        new_like.save()
        post.likes_count = post.likes_count+1
        post.save()
        message = "Post Liked"
    else:
        like_filter.delete()
        post.likes_count = post.likes_count-1
        post.save()
        message = "Post Unliked"
    return JsonResponse({'message': message})

# def report_post(request):
#     post_id = request.GET.get('post_id')
#     username = request.user.username
#     uid = Users.objects.get(username=username)
#     user_id = uid.user_id
#
#     post = Posts.objects.get(post_id=post_id)
#
#     report_filter = Report.objects.filter(post_id=post_id,username=username).first()
#
#     if report_filter == None:
#         new_report = Report.objects.create(post_id=post_id,username=username)
#         new_report.save()
#         post.report_count = post.report_count+1
#         post.save()
#         messages.info(request, "Report submitted")
#         return redirect(reverse('user_post', args=[user_id]))
#     else:
#         messages.info(request,"Report already submitted")
#         return redirect(reverse('user_post', args=[user_id]))

@login_required(login_url='Home')
def report_post_new(request):
    post_id = request.GET.get('post_id')
    username = request.user.username
    uid = Users.objects.get(username=username)
    user_id = uid.user_id

    post = Posts.objects.get(post_id=post_id)

    report_filter = Report.objects.filter(post_id=post_id, username=username).first()

    if report_filter is None:
        new_report = Report.objects.create(post_id=post_id, username=username)
        new_report.save()
        post.report_count = post.report_count + 1
        post.save()
        message = "Report Submitted"
    else:
        message = "Report already Submitted"

    # Redirect to user_post_sample with user_id
    return JsonResponse({'message': message})
    # return redirect('user_post_sample', user_id=user_id)

@login_required(login_url='Home')
def edit_post(request,post_id):
    post = Posts.objects.get(post_id=post_id)
    print("sample")
    username = request.user.username
    print(username)
    uid = Users.objects.get(username=username)
    return render(request,"user/edit_post.html",{'post':post,'user': uid})

@login_required(login_url='Home')
def save_post(request,post_id):
    if request.POST:
        post = Posts.objects.get(post_id=post_id)
        postTitle = request.POST['postTitle']
        postDescription = request.POST['postDescription']
        post.post_title = postTitle
        post.content = postDescription
        post.save()
        username = request.user.username
        uid = Users.objects.get(username=username)

        return redirect(reverse('user_post_new', args=[uid.user_id]))

@login_required(login_url='Home')
def follow(request,followname,user_id):
    username = request.user.username
    followname = followname
    add_follow = Following(user_name=username,following_id=user_id,following=followname)
    add_follow.save()
    uid = Users.objects.get(username=username)
    prof = Profiles.objects.get(user_id=uid.user_id)
    prof.no_of_following = prof.no_of_following + 1
    prof.save()
    prof = Profiles.objects.get(user_id=user_id)
    prof.no_of_followers = prof.no_of_followers + 1
    prof.save()
    return redirect(reverse('user_post_new', args=[uid.user_id]))


@login_required(login_url='Home')
def unfollow(request,followname,user_id):
    username = request.user.username
    unfollow = Following.objects.get(user_name=username,following=followname)
    unfollow.delete()
    uid = Users.objects.get(username=username)
    prof = Profiles.objects.get(user_id=uid.user_id)
    prof.no_of_following = prof.no_of_following - 1
    prof.save()
    prof = Profiles.objects.get(user_id=user_id)
    prof.no_of_followers = prof.no_of_followers - 1
    prof.save()
    messages.info(request, "following")
    return redirect(reverse('edit_profile', args=[uid.user_id]))


@login_required(login_url='Home')
def remove(request,followname,user_id):
    username = request.user.username
    unfollow = Following.objects.get(user_name=followname ,following=username)
    unfollow.delete()
    uid = Users.objects.get(username=followname)
    prof = Profiles.objects.get(user_id=uid.user_id)
    prof.no_of_following = prof.no_of_following - 1
    prof.save()
    prof = Profiles.objects.get(user_id=user_id)
    prof.no_of_followers = prof.no_of_followers - 1
    prof.save()
    return redirect(reverse('edit_profile', args=[user_id]))

@login_required(login_url='Home')
def delete_post(request,post_id):
    post = Posts.objects.get(post_id=post_id)
    post.delete()
    username = request.user.username
    uid = Users.objects.get(username=username)

    prof = Profiles.objects.get(user_id=uid.user_id)
    prof.no_of_posts = prof.no_of_posts - 1
    prof.save()
    return redirect(reverse('Manage Post', args=[uid.user_id]))

@login_required(login_url='adminsignup')
def delete_user(request, id):
    usr = Users.objects.get(user_id=id)
    if Profiles.objects.filter(user_id=id).exists():
        prof = Profiles.objects.get(user_id=id)
        prof.delete()
    if Posts.objects.filter(user_id=id).exists():
        post = Posts.objects.filter(user_id=id)
        post.delete()
    usr.delete()
    username = usr.username
    try:
        user_to_delete = User.objects.get(username=username)
        user_to_delete.delete()
        print(f"User {username} deleted successfully.")
    except User.DoesNotExist:
        print(f"User {username} does not exist.")

    return redirect('/user_list')


def message(request):
    return render(request, 'message.html')

@login_required(login_url='adminsignup')
def edit(request, id):
    uid = Users.objects.get(user_id=id)
    return render(request, 'edit.html', {'user': uid})


# Update Page
@login_required(login_url='adminsignup')
def update(request, usr_id, id):
    uid = Users.objects.get(user_id=id)
    # user_id = request.POST['user_id']
    username = request.POST['signupUsername']
    email = request.POST['email']
    phone_number = request.POST['mobile']
    password = request.POST['signupPassword']

    try:
        # Retrieve the user object with the old username
        user_to_update = User.objects.get(username=uid.username)

        if username != uid.username:
            user_to_update.username = username

        if email != uid.email:
            user_to_update.email = email

        if password != uid.password:
            user_to_update.set_password(password)

        user_to_update.save()

        # uid.user_id =   user_id
        uid.username = username
        uid.email = email
        uid.phone_number = phone_number
        uid.password = password
        uid.save()

        print("User details updated successfully.")
        return redirect('/user_list')
    except User.DoesNotExist:
        print("User does not exist.")

    return redirect('/user_list')


# Login Page
def login(request):
    if request.POST:
        loginUsername = request.POST['loginUsername']
        loginPassword = request.POST['loginPassword']

        user = authenticate(username=loginUsername,password=loginPassword)

        if user is not None:

            auth_login(request,user)
            uid = Users.objects.get(username=loginUsername)
            posts = Posts.objects.exclude(user_id=uid.user_id).order_by('-post_id')
            if hasattr(request.user, 'last_login'):
                last_login_time = request.user.last_login
                uid.last_login_date = timezone.localtime(last_login_time).strftime('%Y-%m-%d %H:%M:%S')
                uid.save()
            followings = Following.objects.filter(user_name=uid.username)

            # Retrieve usernames not in the 'following' queryset
            suggestions = Users.objects.exclude(
                username__in=followings.values_list('following', flat=True)
            ).exclude(user_id=uid.user_id)

            if Following.objects.filter(user_name=uid.username).exists():
                following_ids = [following.following_id for following in followings]
                posts = Posts.objects.exclude(user_id=uid.user_id).order_by('-post_id')
                # return render(request, 'user/user_post.html', {'Posts': posts, 'user': uid, 'follow': suggestions})
                return redirect(reverse('user_post_new', args=[uid.user_id]))
            return redirect(reverse('user_post_new', args=[uid.user_id]))
            # return render(request, 'user/user_post.html', {'user': uid, 'follow': suggestions})
            user_id = str(uid.user_id)
            return redirect('/user_post_new/'+user_id)

        else:
            # messages.error(request,"No User Found")
            messages.error(request, "User not found")
            return redirect('Home')
    else:
        return redirect('Home')

def adminsignup(request):
    return render(request,'admin_login_new.html')
def adminlogin(request):
    if request.POST:
        loginUsername = request.POST['loginUsername']
        loginPassword = request.POST['loginPassword']

        if loginUsername == 'admin':
            user = auth.authenticate(username=loginUsername,password=loginPassword)

            if user is not None:
                auth_login(request,user)
                return redirect('user_list/')
            else:
                return redirect('adminsignup')
        else:
            return redirect('adminsignup')
    else:
        return redirect('adminsignup')

@login_required(login_url='adminsignup')
def logout(request):
    auth.logout(request)
    return redirect('adminsignup')

@login_required(login_url='Home')
def user_logout(request):
    auth.logout(request)
    return redirect('Home')

def logins(request, user_id):
    uid = Users.objects.get(user_id=user_id)
    prof = Profiles.objects.get(user_id=uid.user_id)
    posts = Posts.objects.all()
    return render(request, 'dashboard.html', {'user': uid, 'Profiles': prof, 'Posts': posts})


# Signup Page
def signup(request):
    if request.POST:
        signupUsername = request.POST['signupUsername']
        signupPassword = request.POST['signupPassword']
        confirmPassword = request.POST['confirmPassword']
        mobile = request.POST['mobile']
        email = request.POST['email']
        if signupPassword == confirmPassword:
            uid = Users(username=signupUsername, password=signupPassword, phone_number=mobile, email=email)
            uid.save()
            myuser = User.objects.create_user(signupUsername,email,signupPassword)
            myuser.save()
            posts = Posts.objects.exclude(user_id=uid.user_id).order_by('-post_id')
            # return render(request, 'user/user_post.html', {'user': uid, 'Posts': posts})
            messages.info(request,"Account Successfully Created")
            return render(request, 'index_new.html')
        else:
            print("Not Registered")
            messages.info(request, "Password Does not match")
            return render(request, 'index_new.html')
    else:
        print("Not Registered")
        messages.info(request,"Account Creation Failed")
        return render(request, 'index_new.html')

@login_required(login_url='adminsignup')
def create_user(request):
    if request.POST:
        signupUsername = request.POST['signupUsername']
        signupPassword = request.POST['signupPassword']
        mobile = request.POST['mobile']
        email = request.POST['email']
        user = Users(username=signupUsername, password=signupPassword, phone_number=mobile, email=email)
        user.save()

        myuser = User.objects.create_user(signupUsername,email,signupPassword)
        myuser.save()
        usr = Users.objects.all()  # Default queryset
        return render(request, 'user_list.html', {'Users': usr})
    else:
        print("Not Registered")
        usr = Users.objects.all()  # Default queryset
        return render(request, 'user_list.html', {'Users': usr})
# Save User Profile

@login_required(login_url='Home')
def save_profile(request, user_id):
    if request.POST:
        if Profiles.objects.filter(user_id=user_id).exists():
            prof = Profiles.objects.get(user_id=user_id)

            full_name = request.POST['full_name']
            bio = request.POST['bio']
            profile_picture_url = request.FILES.get('profile_picture_url', None)
            cover_photo_url = request.FILES.get('cover_photo_url', None)
            birthdate = request.POST['date_of_birth']
            gender = request.POST['gender']
            location = request.POST['location']
            prof.full_name = full_name
            prof.bio = bio
            if profile_picture_url:
                prof.profile_picture_url = profile_picture_url
                posts = Posts.objects.filter(user_id=user_id).order_by('-post_id')
                for post in posts:
                    post.profile_picture_url = profile_picture_url
                    post.save()
            if cover_photo_url:
                prof.cover_photo_url = cover_photo_url
            prof.birthdate = birthdate
            prof.gender = gender
            prof.location = location
            prof.save()
            return redirect(reverse('edit_profile', args=[user_id]))
        else:
            user_id = request.POST['user_id']
            # user_id = 1
            full_name = request.POST['full_name']
            bio = request.POST['bio']
            profile_picture_url = request.FILES['profile_picture_url']
            cover_photo_url = request.FILES['cover_photo_url']
            birthdate = request.POST['date_of_birth']
            gender = request.POST['gender']
            location = request.POST['location']
            profile = Profiles(user_id=user_id,
                               full_name=full_name,
                               bio=bio,
                               profile_picture_url=profile_picture_url,
                               cover_photo_url=cover_photo_url,
                               birthdate=birthdate,
                               gender=gender,
                               location=location)
            profile.save()
            return redirect(reverse('edit_profile',args=[user_id]))


def showuser(request):
    usr = Users.objects.all()
    return render(request, 'admin.html', {'Users': usr})


# Admin function
@login_required(login_url='adminsignup')
def user_list(request):
    usr = Users.objects.all()
    return render(request, 'user_list.html', {'Users': usr})

@login_required(login_url='adminsignup')
def sort_user(request, sort_value):
    sort_option = sort_value
    if sort_option == 'user_id':
        usr = Users.objects.order_by('user_id')
    elif sort_option == 'username':
        usr = Users.objects.order_by('username')
    elif sort_option == 'email':
        usr = Users.objects.order_by('email')
    elif sort_option == 'phone_number':
        usr = Users.objects.orderusr_by('phone_number')
    elif sort_option == 'registration_date':
        usr = Users.objects.order_by('registration_date')
    elif sort_option == 'last_login_date':
        usr = Users.objects.order_by('last_login_date')
    else:
        usr = Users.objects.all()  # Default queryset

    return render(request, 'user_list.html', {'Users': usr})

@login_required(login_url='adminsignup')
def search_user(request, search_user):
    uid = Users.objects.filter(username__icontains=search_user)
    return render(request, 'user_list.html', {'Users': uid})

@login_required(login_url='adminsignup')
def search_prof(request, search_prof):
    prof = Profiles.objects.filter(full_name__icontains=search_prof)
    return render(request, 'user_profile.html', {'Profiles': prof})

@login_required(login_url='adminsignup')
def all_user_post(request):
    profiles = Profiles.objects.all().order_by('user_id')
    users = Users.objects.all().order_by('user_id')
    combined_data = zip(profiles, users)
    return render(request, 'all_user_post.html', {'combined_data': combined_data})

@login_required(login_url='adminsignup')
def all_report_post(request):
    # profiles = Profiles.objects.get(user_id=user_id)
    # users = Users.objects.get(user_id=user_id)
    posts = Posts.objects.filter(report_count__gt=0)
    return render(request,'all_report_post.html',{'Posts':posts})
@login_required(login_url='adminsignup')
def view_user_posts(request,user_id):
    profiles = Profiles.objects.get(user_id=user_id)
    users = Users.objects.get(user_id=user_id)
    posts = Posts.objects.filter(user_id=user_id)
    return render(request,'view_user_posts.html',{'Profiles':profiles,'Users':users,'Posts':posts})

@login_required(login_url='adminsignup')
def delete_post_admin(request,post_id):
    post = Posts.objects.get(post_id=post_id)
    uid = Users.objects.get(user_id=post.user_id)

    prof = Profiles.objects.get(user_id=uid.user_id)
    prof.no_of_posts = prof.no_of_posts - 1
    prof.save()
    post.delete()
    return redirect(reverse('view_user_posts', args=[uid.user_id]))

@login_required(login_url='adminsignup')
def delete_post_report_admin(request,post_id):
    post = Posts.objects.get(post_id=post_id)
    uid = Users.objects.get(user_id=post.user_id)

    prof = Profiles.objects.get(user_id=uid.user_id)
    prof.no_of_posts = prof.no_of_posts - 1
    prof.save()
    post.delete()
    return redirect(reverse('all_report_post'))
@login_required(login_url='adminsignup')
def admin_search_user(request, search_user):
    users = Users.objects.filter(username__icontains=search_user).order_by('user_id')
    following_ids = users.values_list('user_id', flat=True)
    profiles = Profiles.objects.filter(user_id__in=following_ids).order_by('user_id')
    combined_data = zip(profiles, users)
    return render(request, 'all_user_post.html', {'combined_data': combined_data})
@login_required(login_url='adminsignup')
def user_profile(request):
    prof = Profiles.objects.all()
    return render(request, 'user_profile.html', {'Profiles': prof})

@login_required(login_url='adminsignup')
def editprof(request, profile_id):
    prof = Profiles.objects.get(profile_id=profile_id)
    return render(request, 'edit_profile.html', {'Profiles': prof})

@login_required(login_url='adminsignup')
def deleteprof(request, profile_id):
    prof = Profiles.objects.get(profile_id=profile_id)
    prof.delete()
    return redirect('/user_profile')

@login_required(login_url='adminsignup')
def updateprof(request, id):
    if request.POST:
        prof = Profiles.objects.get(user_id=id)
        full_name = request.POST['full_name']
        bio = request.POST['bio']
        profile_picture_url = request.FILES.get('profile_picture_url', None)
        print(profile_picture_url)
        cover_photo_url = request.FILES.get('cover_photo_url', None)
        birthdate = request.POST.get('date_of_birth', None)
        gender = request.POST['gender']
        location = request.POST['location']
        prof.full_name = full_name
        prof.bio = bio
        if profile_picture_url:
            prof.profile_picture_url = profile_picture_url
            print(profile_picture_url)
        if cover_photo_url:
            prof.cover_photo_url =  cover_photo_url
        prof.birthdate = birthdate
        prof.gender = gender
        prof.location = location
        prof.save()
        return redirect('/user_profile')

@login_required(login_url='adminsignup')
def sort_prof(request, sort_value):
    sort_option = sort_value
    if sort_option == 'profile_id':
        prof = Profiles.objects.order_by('profile_id')
    elif sort_option == 'user_id':
        prof = Profiles.objects.order_by('user_id')
    elif sort_option == 'full_name':
        prof = Profiles.objects.order_by('full_name')
    elif sort_option == 'bio':
        prof = Profiles.objects.order_by('bio')
    elif sort_option == 'birthdate':
        prof = Profiles.objects.order_by('birthdate')
    elif sort_option == 'gender':
        prof = Profiles.objects.order_by('gender')
    elif sort_option == 'location':
        prof = Profiles.objects.order_by('location')
    elif sort_option == 'created_at':
        prof = Profiles.objects.order_by('created_at')
    else:
        prof = Profiles.objects.all()  # Default queryset

    return render(request, 'user_profile.html', {'Profiles': prof})


def json(request):
#     data = list(Posts.objects.values())
#     return JsonResponse(data,safe=False)
#     return render(request, 'sample.html', {'data': data})
    return render(request, 'sample.html')

@login_required(login_url='adminsignup')
def charts(request):
    # Querying data from the Users model
    users_data = Profiles.objects.all()

    # Extracting user attributes from the queryset
    attributes = ['full_name', 'no_of_followers', 'no_of_following', 'no_of_posts']
    data = {attr: [getattr(user, attr) for user in users_data] for attr in attributes}

    # Passing data to the template
    return render(request, "charts.html", {'data': data})



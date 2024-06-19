from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='Home'),

    path('logout',views.logout),
# User Urls ---------------------------------------------------------
#     path('user_nav/',views.user_nav),
#     path('user_post/<int:user_id>',views.user_post,name="user_post"),
    path('login', views.login, name='login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('add_post/<int:user_id>',views.add_post_view),
    path('add_posts/<int:user_id>',views.add_post,name="Add Post"),
    path('manage_post/<int:user_id>',views.manage_post,name="Manage Post"),
    path('edit_profile/<int:user_id>',views.edit_profile,name="edit_profile"),
    # path('like_post/',views.like_post,name="like_post"),
    path('like_post_new/',views.like_post_new,name="like_post_new"),

    path('add_comment/', views.add_comment, name='add_comment'),
    path('get_comment/', views.get_comment, name="get_comment"),

    path('delete_post/<int:post_id>',views.delete_post,name="delete_post"),
    path('edit_post/<int:post_id>',views.edit_post,name="edit_post"),
    path('save_post/<int:post_id>',views.save_post,name="save_post"),
    path('follow/<str:followname>_<int:user_id>',views.follow,name="follow"),
    path('unfollow/<str:followname>_<int:user_id>',views.unfollow,name="unfollow"),
    path('remove/<str:followname>_<int:user_id>',views.remove,name="remove"),
    path('following/',views.following,name="following"),
    path('followers/',views.followers,name="followers"),
    path('save_profile/<int:user_id>/',views.save_profile,name="Save User Profile"),
    path('search_profile/',views.search_profile,name="search_profile"),
    path('search_profiles/<str:user_name>',views.search_profiles,name="search_profile"),
    # path('report_post/', views.report_post, name="report_post"),
    path('report_post_new/', views.report_post_new, name="report_post_new"),

    path('user_post_new/<int:user_id>', views.user_post_new, name="user_post_new"),
    path('user_post_sample/<int:user_id>', views.user_post_sample, name="user_post_sample"),
    # path('json/',views.json,name="json"),
    # path('get_post/<int:user_id>/',views.get_post,name="get_post"),


# Admin Urls --------------------------------------------------------

    path('adminlogin', views.adminlogin, name='Admin login'),
    path('adminsignup', views.adminsignup, name='adminsignup'),

    path('user_list/',views.user_list),
    path('create_user', views.create_user),
    path('user_list/edit/<int:id>/', views.edit, name='Edit'),
    path('user_list/edit/<int:usr_id>/update/<int:id>/', views.update, name='Update'),
    path('user_list/delete/<int:id>',views.delete_user),
    path('user_list/12_<str:sort_value>',views.sort_user),
    path('user_list/13_<str:search_user>',views.search_user),

    
    path('user_profile/',views.user_profile),
    path('user_profile/editprof/<int:profile_id>',views.editprof),
    path('user_profile/deleteprof/<int:profile_id>',views.deleteprof),
    path('user_profile/editprof/updateprof/<int:id>/', views.updateprof, name='Update'),
    path('user_profile/12_<str:sort_value>', views.sort_prof),
    path('user_profile/13_<str:search_prof>', views.search_prof),


    path('all_user_post/', views.all_user_post,name='all_user_post'),
    path('view_user_posts/<int:user_id>', views.view_user_posts,name="view_user_posts"),
    path('delete_post_admin/<int:post_id>',views.delete_post_admin,name="delete_post_admin"),
    path('delete_post_report_admin/<int:post_id>',views.delete_post_report_admin,name="delete_post_report_admin"),
    path('admin_search_user/13_<str:search_user>',views.admin_search_user,name="admin_search_user"),
    path('all_report_post/', views.all_report_post, name='all_report_post'),
    # User Urls----------------------------------------------------

    path('charts', views.charts),

    # path('index/',views.index),

# add post

#     login form link
#     path('logins<int:user_id>',views.logins,name='logins'),

#     signup form link
    path('signup',views.signup),
#     User list Request
#     path('showuser',views.showuser),

]

# if settings.DEBUG:
#     urlpatterns+=static(settings.media_urls)


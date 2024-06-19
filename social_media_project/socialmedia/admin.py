from django.contrib import admin
from .models import *


admin.site.register(Users)
admin.site.register(Profiles)
admin.site.register(Following)
admin.site.register(Posts)
admin.site.register(Report)
admin.site.register(Likes)
admin.site.register(Messages)
admin.site.register(Grouptbl)
admin.site.register(SearchHistory)
admin.site.register(Comments)
admin.site.register(Notifications)











# Get all model classes from the models module
# model_classes = [obj for name, obj in vars().items() if isinstance(obj, type)]
#
# # Register all model classes
# for model_class in model_classes:
#     admin.site.register(model_class)

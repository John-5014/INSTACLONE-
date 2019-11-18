from django.contrib import admin
from .models import Profile,Post,Comment,Location,Like,Follow

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Location)
admin.site.register(Like)
admin.site.register(Follow)

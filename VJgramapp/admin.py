from django.contrib import admin
from .models import Post,Friend,Comment,Like
# Register your models here.
admin.site.register(Post)
admin.site.register(Friend)
admin.site.register(Comment)

admin.site.register(Like)

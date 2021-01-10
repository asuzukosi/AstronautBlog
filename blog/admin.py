from django.contrib import admin
from .models import Post, Author, Series, Subscriber, Comment, Category, Likes, Save


# Register your models here.
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Series)
admin.site.register(Subscriber)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Likes)
admin.site.register(Save)

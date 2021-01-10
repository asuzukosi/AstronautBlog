from django.db import models
from django.contrib.auth.models import User
import datetime
from ckeditor.fields import RichTextField
import random
# Create your models here.


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        u = self.user
        return f'{u.first_name} {u.last_name}'

    def get_posts(self):
        posts = Post.objects.filter(author=self)
        return posts


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_posts(self):
        posts = Post.objects.filter(category=self)
        return posts


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField(blank=True, null=True)
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_written = models.DateTimeField()
    title_image = models.URLField(default="")

    def __str__(self):
        return f'{self.title} by {self.author}'

    def get_num_likes(self):
        likes = Likes.objects.filter(post=self)
        return len(likes)

    def get_next_post(self):
        posts = Post.objects.all()
        for x in range(len(posts)):
            if x == len(posts)-1:
                return posts[0]
            if posts[x] == self:
                return posts[x+1]

    def get_related_posts(self):
        posts_set = set()
        posts = []

        for category in self.category.all():
            cat_list = Post.objects.filter(category=category).exclude(title=self.title)
            posts_set.update(cat_list)

        for post in posts_set:
            posts.append(post)

        random.shuffle(posts)

        return posts[:3]

    def get_categories(self):
        categories = self.category.all()
        return categories

    def like_post(self, subscriber):
        like = Likes(suscriber=subscriber, post=self)
        like.date_liked = datetime.datetime.now()
        like.save()

    def save_post(self, subscriber):
        sv = Save(suscriber=subscriber, post=self)
        sv.date_liked = datetime.datetime.now
        sv.save()

    def unlike_post(self, subscriber):
        like = Likes.objects.get(suscriber=subscriber, post=self)
        like.delete()

    def unsave_post(self, subscriber):
        sv = Save.objects.get(suscriber=subscriber, post=self)
        sv.delete()

    def get_comments(self):
        comments = Comment.objects.filter(post=self)
        return comments


class Series(models.Model):
    name = models.CharField(max_length=200)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return self.name

    def num_likes(self):
        likes = 0
        post_list = self.posts.all()
        for post in post_list:
            likes += post.get_num_likes()

        return likes

    def num_posts(self):
        return len(self.posts.all())


class Subscriber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        u = self.user
        return f'{u.first_name} {u.last_name}'

    def get_saved_posts(self):
        posts = Save.objects.filter(suscriber=self)
        return posts

    def get_liked_posts(self):
        posts = Likes.objects.filter(suscriber=self)
        return posts

    def saved_this_post(self, post):
        try:
            save = Save.objects.get(suscriber=self, post=post)
            return True
        except:
            return False

    def liked_this_post(self, post):
        try:
            like = Likes.objects.get(suscriber=self, post=post)
            return True
        except:
            return False


class Comment(models.Model):
    text = models.CharField(max_length=200)
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_written = models.DateTimeField()

    def __str__(self):
        return f' {self.text[:10]} by {self.subscriber} '


class Likes(models.Model):
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_liked = models.DateTimeField()

    def __str__(self):
        return f'{self.subscriber} liked {self.post}'


class Save(models.Model):
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_liked = models.DateTimeField()

    def __str__(self):
        return f'{self.subscriber} liked {self.post}'

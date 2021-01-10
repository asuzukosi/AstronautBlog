from django.urls import path
from . import views
# Create url patterns

urlpatterns = [
    path("", views.home, name="Home"),
    path("about", views.about, name="About"),
    path("contact", views.contact, name="Contact"),
    path("store", views.store, name="Store"),
    path("article/<int:post_pk>", views.article, name="Article"),
    path("series", views.series, name="Series"),
    path("posts", views.posts, name="Posts"),
]
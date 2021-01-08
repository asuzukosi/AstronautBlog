from django.urls import path
from . import views
# Create url patterns

urlpatterns = [
    path("", views.home, name="Home")
]
from django.urls import path

from . import views

urlpatterns = [
    path("all", views.show_blogs, name="all"),
    path("create_blog", views.create_blog, name="create"),
]
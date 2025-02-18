from django.urls import path
from . import views

app_name = "hyperion"
urlpatterns = [
	path("", views.home, name="home"),
	path("about/", views.about, name="about"),
	path("blog/<int:pk>", views.blog, name="blog")
]

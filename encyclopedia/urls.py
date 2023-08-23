from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:text>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("new/", views.new_page, name="new_page"),
    path("edit/", views.edit, name="edit"),
    path("save/", views.save, name="save"),
    path("random/", views.random_page, name="random_page")
]

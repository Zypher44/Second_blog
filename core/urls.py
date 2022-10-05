from django.urls import path

from . import views

urlpatterns = [
    path("core/", views.index_core, name="index"),
]

from django.urls import path
from . import views

urlpatterns = [
    path("sync/", views.createEntry1, name="create_entry"),
    path("thread/", views.createEntry1, name="create_entry"),
    path("txn/", views.createEntry3, name="create_entry"),
]
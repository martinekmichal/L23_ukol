from django.urls import path
from .views import *

urlpatterns = [
    path("user_foto/<int:pk>/", UserFotoView.as_view(), name="user_foto"),
    path("user_list/", UserListView.as_view(), name="user_list"),
    path("create_foto/", CreateFotoView.as_view(), name="create_foto"),
]
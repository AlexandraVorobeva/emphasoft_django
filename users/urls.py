from django.urls import path

from .views import UserList, UserDetail

urlpatterns = [
    path("all", UserList.as_view(), name="all-users"),
    path("<int:pk>/", UserDetail.as_view(), name="user"),
]

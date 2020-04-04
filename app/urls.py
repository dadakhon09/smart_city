from django.urls import path

from app.users.views import UserLogin, UserLogout, UserCreate, UserListAPIView, UserUpdateAPIView, UserDeleteAPIView

urlpatterns = [

    path('users/login/', UserLogin.as_view(), name='login'),
    path('users/logout/', UserLogout.as_view(), name='logout'),
    path('users/create', UserCreate.as_view(), name='create-user'),
    path('users/list/', UserListAPIView.as_view(), name='users-list'),
    path('users/list/<int:id>/update/', UserUpdateAPIView.as_view(), name='user-update'),
    path('users/list/<int:id>/delete/', UserDeleteAPIView.as_view(), name='user-delete'),
]
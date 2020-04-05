from django.urls import path

from app.complain.views import ComplainsList, ComplainDelete, ComplainCreate, ComplainUpdate, ComplainList
from app.users.views import UserLogin, UserLogout, UserCreate, UserListAPIView, UserUpdateAPIView, UserDeleteAPIView

urlpatterns = [

    path('users/login/', UserLogin.as_view(), name='login'),
    path('users/logout/', UserLogout.as_view(), name='logout'),
    path('users/create/', UserCreate.as_view(), name='create-user'),
    path('users/list/', UserListAPIView.as_view(), name='users-list'),
    path('users/list/<int:id>/update/', UserUpdateAPIView.as_view(), name='user-update'),
    path('users/list/<int:id>/delete/', UserDeleteAPIView.as_view(), name='user-delete'),

    path('complains/list/', ComplainsList.as_view(), name='complains-list'),
    path('complains/list/', ComplainCreate.as_view(), name='complain-create'),
    path('complains/list/<int:id>/', ComplainList.as_view(), name='complain-list'),
    path('complains/list/<int:id>/update/', ComplainUpdate.as_view(), name='complain-update'),
    path('complains/list/<int:id>/delete/', ComplainDelete.as_view(), name='complain-delete'),

]
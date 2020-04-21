from django.urls import path

from app.complain.views import ComplainsList, ComplainDelete, ComplainCreate, ComplainUpdate, ComplainList
from app.category.views import CategoriesList, CategoryDelete, CategoryCreate, CategoryUpdate, CategoryList
from app.sub_category.views import SubCategoriesList, SubCategoryDelete, SubCategoryCreate, SubCategoryUpdate, SubCategoryList
from app.users.views import UserLogin, UserLogout, UserCreate, UserListAPIView, UserUpdateAPIView, UserDeleteAPIView

urlpatterns = [

    path('users/login/', UserLogin.as_view(), name='login'),
    path('users/logout/', UserLogout.as_view(), name='logout'),
    path('users/create/', UserCreate.as_view(), name='create-user'),
    path('users/list/', UserListAPIView.as_view(), name='users-list'),
    path('users/list/<int:id>/update/', UserUpdateAPIView.as_view(), name='user-update'),
    path('users/list/<int:id>/delete/', UserDeleteAPIView.as_view(), name='user-delete'),

    path('complains/list/', ComplainsList.as_view(), name='complains-list'),
    path('complains/create/', ComplainCreate.as_view(), name='complain-create'),
    path('complains/list/<int:id>/', ComplainList.as_view(), name='complain-list'),
    path('complains/list/<int:id>/update/', ComplainUpdate.as_view(), name='complain-update'),
    path('complains/list/<int:id>/delete/', ComplainDelete.as_view(), name='complain-delete'),

    path('categories/list/', CategoriesList.as_view(), name='categories-list'),
    path('categories/create/', CategoryCreate.as_view(), name='category-create'),
    path('categories/list/<int:id>/', CategoryList.as_view(), name='category-list'),
    path('categories/list/<int:id>/update/', CategoryUpdate.as_view(), name='category-update'),
    path('categories/list/<int:id>/delete/', CategoryDelete.as_view(), name='category-delete'),

    path('sub_categories/list/', SubCategoriesList.as_view(), name='sub_categories-list'),
    path('sub_categories/create/', SubCategoryCreate.as_view(), name='sub_category-create'),
    path('sub_categories/list/<int:id>/', SubCategoryList.as_view(), name='sub_category-list'),
    path('sub_categories/list/<int:id>/update/', SubCategoryUpdate.as_view(), name='sub_category-update'),
    path('sub_categories/list/<int:id>/delete/', SubCategoryDelete.as_view(), name='sub_category-delete'),
]
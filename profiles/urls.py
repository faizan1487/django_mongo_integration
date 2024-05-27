from django.urls import path
from .views import UserProfileListCreate, UserProfileRetrieveUpdateDestroy

urlpatterns = [
    path('profiles/', UserProfileListCreate.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', UserProfileRetrieveUpdateDestroy.as_view(), name='profile-detail'),
    path('delete_user_profile/<str:user_profile_id>/', views.delete_user_profile, name='delete_user_profile'),

]

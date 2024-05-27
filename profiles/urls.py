from django.urls import path
from .views import UserProfileListCreate, UserProfileRetrieveUpdateDestroy

urlpatterns = [
    path('profiles/', UserProfileListCreate.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', UserProfileRetrieveUpdateDestroy.as_view(), name='profile-detail'),
]

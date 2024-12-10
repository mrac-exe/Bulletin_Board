from django.urls import path

from .views import ConfirmUser, ProfileView

urlpatterns = [
    path('confirm/', ConfirmUser.as_view(), name='confirm_user'),
    path('profile/', ProfileView.as_view(), name='profile'),
]

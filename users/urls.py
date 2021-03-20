from django.urls import path

from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView

app_name = 'users'
urlpatterns = [
    path('user', UserRetrieveUpdateAPIView.as_view()),
    path('users/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
]
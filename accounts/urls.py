from django.urls import path
from .views import LoginAPI, RegisterAPI, RegisterConfirmAPI, CreateUserAPIView, LogoutAPIView, \
    AccountDetailCreateAPIView, AccountDetailListAPIView

urlpatterns = [
    path('login/', LoginAPI.as_view()),
    path('register/', RegisterAPI.as_view()),
    path('register-confirm/', RegisterConfirmAPI.as_view()),
    path('create-user/', CreateUserAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
    path('create-detail/', AccountDetailCreateAPIView.as_view()),
    path("detail-list/", AccountDetailListAPIView.as_view())
]

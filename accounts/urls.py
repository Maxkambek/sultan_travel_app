from django.urls import path
from .views import LoginAPI, RegisterAPI, RegisterConfirmAPI, LoginConfirmAPI, LogoutAPIView, \
    AccountDetailCreateAPIView, AccountDetailListAPIView, AccountRetrieveAPIView

urlpatterns = [
    path('login/', LoginAPI.as_view()),
    path('register/', RegisterAPI.as_view()),
    path('register-confirm/', RegisterConfirmAPI.as_view()),
    path('login-confirm/', LoginConfirmAPI.as_view()),
    path('logout/', LogoutAPIView.as_view()),
    path('create-detail/', AccountDetailCreateAPIView.as_view()),
    path("detail-list/", AccountDetailListAPIView.as_view()),
    path('account/<int:pk>/', AccountRetrieveAPIView.as_view())
]

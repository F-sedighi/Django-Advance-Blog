from django.urls import path
from .. import views

# from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    # Registration
    path(
        "registration/",
        views.RegistrationApiView.as_view(),
        name="registration",
    ),
    path("test-email", views.TestEmailSend.as_view(), name="test-email"),
    # Activation
    path(
        "activation/confirm/<str:token>",
        views.ActivationApiView.as_view(),
        name="activation",
    ),
    # Resend activation
    path(
        "activation/resend/",
        views.ActivaitonResendApiView.as_view(),
        name="activation-resend",
    ),
    # Change password
    path(
        "change-password/",
        views.ChangePasswordApiView.as_view(),
        name="change-password",
    ),
    # Reset password
    # Login token
    # path('token/login/', ObtainAuthToken.as_view(), name = 'token-login'),
    path(
        "token/login/",
        views.CustomObtainAuthToken.as_view(),
        name="token-login",
    ),
    # Logout token
    path(
        "token/logout/",
        views.CustomDiscardAuthToken.as_view(),
        name="token-logout",
    ),
    # Create token
    # path('/jwt/create/', TokenObtainPairView.as_view(), name = 'jwt-create'),
    path(
        "/jwt/create/",
        views.CustomTokenObtainPairView.as_view(),
        name="jwt-create",
    ),
    # Refresh token
    path("/jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    # Verify token
    path("/jwt/verify/", TokenVerifyView.as_view(), name="jwt-verify"),
]

from django.urls import path, include
from .views import Profile, LogoutView, SignInView, SignUpView

urlpatterns = [
    path("profile/", Profile.as_view(), name="profile"),
    # path("profile/", include("django.contrib.auth.urls")),
    path("signin/", SignInView.as_view(), name="sign_in"),
    path("signup/", SignUpView.as_view(), name="sign_up"),
    path("logout/", LogoutView.as_view(), name="log_out"),
]
#     path("signin/", SignInView.as_view(), name="sign_in"),
#     path("signup/", SignUpView.as_view(), name="sign_up"),
#     path("logout/", LogoutView.as_view(), name="log_out"),

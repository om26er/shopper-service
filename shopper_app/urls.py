from django.conf.urls import url

from shopper_app.views import (
    ActivationKeyRequest,
    ForgotPassword,
    ChangePassword,
    Register,
    Login,
    Activate,
    Profile,
    StatusAPIView
)


urlpatterns = [
    url(r'^api/user/register$', Register.as_view()),
    url(r'^api/user/request-activation-key$', ActivationKeyRequest.as_view()),
    url(r'^api/user/activate$', Activate.as_view()),
    url(r'^api/user/login$', Login.as_view()),
    url(r'^api/user/forgot-password$', ForgotPassword.as_view()),
    url(r'^api/user/change-password$', ChangePassword.as_view()),
    url(r'^api/user/status$', StatusAPIView.as_view()),
    url(r'^api/me$', Profile.as_view()),
]

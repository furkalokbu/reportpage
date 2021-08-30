from django.contrib import admin
from django.urls import path
from django.urls.conf import include, path
from users.forms import CustomUserForm

from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # registration new account by django_registration
    path("accounts/register/",
    RegistrationView.as_view(
        form_class = CustomUserForm,
        success_url = "/",
    ), name="django_registration_register"),

    # login by django_registration
    path("accounts/",
    include("django_registration.backends.one_step.urls")),

    # login urls by Django
    path("accounts/",
    include("django.contrib.auth.urls")),

    # login browser api
    path("api-auth/",
    include("rest_framework.urls")),

    # login REST
    path("api/rest-auth/",
    include("rest_auth.urls")),

    # registration REST
    path("api/rest-auth/registration/",
    include("rest_auth.registration.urls")),

]

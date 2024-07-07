# from django.contrib import admin
from django.urls import path
from accounts.views import login_page

# from django.conf import settings
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("login/", login_page, name="login"),
]

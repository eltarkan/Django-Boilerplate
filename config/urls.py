from django.contrib import admin
from django.urls import path, include
from applications.api.users.router import urlpatterns as user_router

admin.autodiscover()

urlpatterns = [
    path('token/', include(user_router))
]

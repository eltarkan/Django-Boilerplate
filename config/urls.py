from django.contrib import admin
from django.urls import path, include
from applications.api.router import router

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

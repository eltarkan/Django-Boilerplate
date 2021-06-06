from django.contrib import admin
from django.urls import path, include
from applications.api.intel_requirement.router import urlpatterns as intel_router
from applications.api.users.router import urlpatterns as user_router

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i-need-intel/', include(intel_router)),
    path('token/', include(user_router))
]

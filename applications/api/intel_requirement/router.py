from applications.api.intel_requirement.views import IntelligenceRequirementFormViewSet
from django.urls import path, include

urlpatterns = [
    path('', IntelligenceRequirementFormViewSet.as_view({"get": "list", "post": "create"}))
]

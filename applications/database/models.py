from django.db import models
from applications.api.constants import IntelTypeCode


class IntelRequirementForm(models.Model):

    user_code = models.CharField(max_length=64)
    intelligence_type_code = models.CharField(choices=IntelTypeCode, max_length=64)
    subject = models.CharField(max_length=64)
    content = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

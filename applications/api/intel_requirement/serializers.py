from rest_framework import serializers
from applications.database.models import IntelRequirementForm
from applications.api.constants import IntelTypeCode

import base64
import json


class IntelligenceRequirementFormSerializer(serializers.ModelSerializer):
    intelligence_type_code = serializers.CharField(
        max_length=2,
        help_text=IntelTypeCode
    )
    subject = serializers.CharField(max_length=1024)
    content = serializers.JSONField()

    class Meta:
        model = IntelRequirementForm
        fields = ["user_code", "intelligence_type_code", "subject", "content"]

    def create(self, validated_data):
        return IntelRequirementForm.objects.create(**self.encrypt_data(validated_data))

    def encrypt_data(self, validated_data):
        """Its simple because base64 encryption"""
        restored_data = {
            "user_code": validated_data["user_code"],
            "intelligence_type_code": base64.b64encode(validated_data["intelligence_type_code"].encode("ascii")),
            "subject": base64.b64encode(validated_data["subject"].encode("ascii")),
            "content": base64.b64encode(json.dumps(validated_data["content"]).encode("ascii"))
        }
        return restored_data

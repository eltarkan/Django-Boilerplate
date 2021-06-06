from rest_framework import viewsets, permissions
from rest_framework.response import Response
from applications.database.models import IntelRequirementForm
from applications.api.intel_requirement.serializers import IntelligenceRequirementFormSerializer
import logging


# ViewSets define the view behavior.
class IntelligenceRequirementFormViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        queryset = IntelRequirementForm.objects.all()
        serializer = IntelligenceRequirementFormSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        # todo: return response must be check
        serializer = IntelligenceRequirementFormSerializer(data=request.data)

        if serializer.is_valid():
            try:
                IntelRequirementForm.objects.create(serializer.data)
            except Exception as e:
                logging.error(e)
            return Response({})
        else:
            return Response({"error": serializer.errors})

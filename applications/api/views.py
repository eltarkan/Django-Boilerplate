from rest_framework import viewsets
from applications.database.models import Cars
from applications.api.serializers import CarSerializer


# ViewSets define the view behavior.
class CarViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer

from rest_framework.response import Response 

from .models import Application
from .serializer import ApplicationSerializer 
from rest_framework.viewsets import ModelViewSet


class ApplicationViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

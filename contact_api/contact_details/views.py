from .models import *
from rest_framework.viewsets import ModelViewSet
from .serializers import ContactSerailizer


class ContactView(ModelViewSet):
    queryset = contact_det.objects.all()
    serializer_class = ContactSerailizer
    
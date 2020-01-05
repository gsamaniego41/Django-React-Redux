from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

# Lead Viewset

class LeadViewSet(viewsets.ModelViewSet):
  '''
  Viewsets allow us to create a full CRUD API
  without having to specify explicit methods
  for the functionality
  '''
  queryset = Lead.objects.all() # Gets all the leads
  permission_classes = [
    permissions.AllowAny
  ]
  serializer_class = LeadSerializer
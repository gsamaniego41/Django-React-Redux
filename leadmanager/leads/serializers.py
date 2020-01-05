from rest_framework import serializers
from leads.models import Lead

# Lead Serializer
class LeadSerializer(serializers.ModelSerializer):
  '''
  Serializers allow complex data such as querysets and model
  instances to be converted to native Python datatypes that can then
  be easily rendred into JSON, XML, or other content types.
  '''
  class Meta:
    model = Lead
    fields = '__all__'
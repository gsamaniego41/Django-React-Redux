from django.db import models

# Create your models here.
class Lead(models.Model):
  name = models.CharField(max_length=100) 
  email = models.EmailField(max_length=100, unique=True)
  # blank=True makes it optional
  message = models.CharField(max_length=500, blank=True)
  # auto_now_add=True will add the date automatically
  created_at = models.DateTimeField(auto_now_add=True) 
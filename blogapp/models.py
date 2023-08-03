from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.




class Name(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
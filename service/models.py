from django.db import models

class Service(models.Model):
    Service_icon=models.CharField(max_length=50)
    Service_title=models.CharField(max_length=50)
    Service_desc=models.TextField()


# Create your models here.

from django.db import models

# Create your models here.
class studetail(models.Model):
    name = models.CharField(max_length=20)
    school = models.CharField(max_length=20)


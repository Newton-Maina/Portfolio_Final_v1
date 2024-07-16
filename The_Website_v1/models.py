from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    case_name = models.CharField(max_length=200)
    description = models.TextField()
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/')



# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.name

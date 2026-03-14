from django.db import models

# Create your models here.
class Phones(models.Model):
    phone = models.CharField(max_length=50)
    memory = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    image = models.ImageField(upload_to='phones/')
    price = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.phone



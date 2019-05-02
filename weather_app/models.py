from django.db import models

# Create your models here.
class City(models.Model):
    city_name=models.CharField(max_length=30)
    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name_plural='cities'

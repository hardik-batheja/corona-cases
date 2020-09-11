from django.db import models

# Create your models here.
class Country(models.Model):
    country=models.CharField(max_length=100,unique=True)
    countrycode=models.IntegerField()
    tcases=models.IntegerField()
    rcases=models.IntegerField()
    dcases=models.IntegerField()

    def __str__(self):
        return self.country
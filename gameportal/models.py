from django.db import models

class Game(models.Model):
    url_name = models.CharField(max_length=30,null=True,blank=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    release_date = models.DateField()
    rating = models.IntegerField()
    img_name = models.CharField(max_length=100,null=True,blank=True)

    
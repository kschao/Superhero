from django.db import models

# Create your models here.
class Superhero(models.Model):
    superhero_pic = models.CharField(max_length=100)
    superheros_names = models.CharField(max_length=50)
    alter_ego_name = models.CharField(max_length=50)
    prim_ability = models.CharField(max_length=75)
    second_ability = models.CharField(max_length=75)
    catchphrase = models.CharField(max_length=100)
    runtime = models.IntegerField()
    release_date = models.DateField()

    def __str__(self):
        return self.superheros_names
        
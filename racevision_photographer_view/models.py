from django.db import models

class Runner(models.Model):
    
    place = models.IntegerField(max_length=4, unique = True)
    n_jersey = models.IntegerField(max_length=4, unique = True)
    name = models.CharField(max_length = 100)
    n_licence = models.DateField(null = False)
    club = models.CharField(max_length = 100)
    image = models.FileField(upload_to = 'images/', blank = True)
    netTiming = models.TimeField(null = False)
    place = models.IntegerField(max_length=4, unique = True)
    def __str__(self):
        return str(self.name)
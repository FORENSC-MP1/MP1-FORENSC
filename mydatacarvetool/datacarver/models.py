from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Filesig(models.Model):
    header = models.CharField(max_length=200)
    trailer = models.CharField(max_length=200, blank=True)
    filetype = models.CharField(max_length=50)
    status = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.filetype

class information(models.Model):
    dircopy = models.CharField(max_length=50)
    dirsave = models.CharField(max_length=50)
    sector = models.IntegerField(default=512)
    maxsize = models.IntegerField(default=10000000, 
                                  validators=[
                                      MaxValueValidator(50000000),
                                      MinValueValidator(1000)
                                  ])
    threads = models.IntegerField(default=100,validators=[
                                     MinValueValidator(10)
                                  ])
    workers = models.IntegerField(default=100,validators=[
                                     MinValueValidator(10)
                                  ])
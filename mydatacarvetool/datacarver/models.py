from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Filesig(models.Model):
    header = models.CharField(max_length=200)
    trailer = models.CharField(max_length=200, blank=True)
    filetype = models.CharField(max_length=50)
    status = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.filetype.upper().replace(".","")

class information(models.Model):
    dircopy = models.CharField(max_length=50)
    dirsave = models.CharField(max_length=50)
    sector = models.IntegerField(default=512)
    maxsize = models.IntegerField(default=10000000, 
                                  validators=[
                                      MaxValueValidator(5000000000),
                                      MinValueValidator(1)
                                  ])
    nMax = models.IntegerField(default=1000000,
                                  validators=[
                                      MaxValueValidator(125000000),
                                      MinValueValidator(1)
                                  ])
    threads = models.IntegerField(default=10,validators=[
                                     MinValueValidator(10)
                                  ])
    workers = models.IntegerField(default=10,validators=[
                                     MinValueValidator(10)
                                  ])
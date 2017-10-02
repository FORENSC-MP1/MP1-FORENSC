from django.db import models

# Create your models here.
class Filesig(models.Model):
    header = models.CharField(max_length=200)
    trailer = models.CharField(max_length=200)
    filetype = models.CharField(max_length=50)
    status = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.filetype

from django.db import models


# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    #field=('name' ,'text', 'desc)

    def __str__(self):

        return self.name
class Team(models.Model):
    #name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=250)
    desc = models.TextField()


    # def __init__(self, *args, **kwargs):
    #     super().__init__(args, kwargs)
    #     self.name = None

    def __str__(self):

        return self.name
from django.db import models

# Create your models here.

class Movie(models.Model):
  img = models.ImageField(upload_to='pics')
  title = models.CharField(max_length=100)
  year = models.IntegerField()
  desc = models.TextField()

  
class Schedule(models.Model):
  date = models.DateField()
  time = models.TimeField()
  movie = models.ForeignKey(Movie, null=True, on_delete= models.SET_NULL)
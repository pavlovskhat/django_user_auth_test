from django.db import models


# Create your models here.
class Band(models.Model):
	name = models.CharField(max_length=100)
	album = models.CharField(max_length=100)
	year_of_origin = models.IntegerField()

	def __str__(self):
		return self.name

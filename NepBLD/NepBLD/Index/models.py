from django.db import models
from autoslug import AutoSlugField



class RegisterClass(models.Model):
	first_name = models.CharField(max_length=100, verbose_name='First Name')
	middle_name = models.CharField(max_length=100, verbose_name='Middle Name')
	last_name = models.CharField(max_length=100,  verbose_name='last Name')
	name_slug = AutoSlugField(populate_from='first_name', unique_with=['first_name','last_name'])

	def __str__(self):
		return self.first_name

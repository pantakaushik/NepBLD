from django.db import models
from autoslug import AutoSlugField

gender_choices = (
	('male','male'),
	('female','female'),
	('unknown','unknown'),
	)
blood_group = (
	('A','A'),
	('B','B'),
	('O','O'),
	('AB','AB'),
	)
city = (
	('narayanghat','narayanghat'),
	('pokhara','pokhara'),
	('kathmandu','kathmandu'),
	('biratnagar','biratnagar'),
	)

class RegisterClass(models.Model):
	first_name = models.CharField(max_length=100, verbose_name='First Name')
	middle_name = models.CharField(max_length=100, verbose_name='Middle Name', blank=True)
	last_name = models.CharField(max_length=100,  verbose_name='last Name')
	name_slug = AutoSlugField(populate_from='first_name', unique_with=['first_name','last_name'])
	gender = models.CharField(max_length=6, verbose_name='Gender', choices=gender_choices)
	bloodgroup = models.CharField(max_length=4, verbose_name='Blood group',choices=blood_group)
	city = models.CharField(max_length=50, verbose_name='City', choices=city)
	address = models.CharField(max_length=50, verbose_name='Address')
	email = models.EmailField(verbose_name="Email")
	contact_number = models.CharField(max_length=10,verbose_name="Contact Number")




	def __str__(self):
		return self.first_name

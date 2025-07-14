from django.db import models
from project_implementation.models import *
from froala_editor.fields import FroalaField
from news.models import Category

# Create your models here.

class Activities(models.Model):
	title = models.CharField(max_length = 300, verbose_name='Title')
	activity_content = FroalaField(verbose_name='Activity Content')
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='get_category', verbose_name='Category')
	image = models.ImageField(upload_to='Posts/', null=True)
	years=models.ForeignKey(Year, on_delete=models.CASCADE, related_name='years', verbose_name='Tinan')
	date=models.DateField(verbose_name='Data Implemetasaun')

	class Meta:
		verbose_name = 'actividade'
		verbose_name_plural = 'actividades'
		ordering = ['-date']

	def __str__(self):
		return self.activity_content

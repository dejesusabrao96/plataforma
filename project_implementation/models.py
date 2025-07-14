from django.db import models

# Create your models here.
class Year(models.Model):
	year=models.CharField(max_length=10, verbose_name='Tinan')
	
	def __str__(self):
		return self.year

class ProjectImplementation(models.Model):
	years=models.ForeignKey(Year, on_delete=models.CASCADE, related_name='get_year', verbose_name='Tinan')
	date=models.DateField(verbose_name='Data Implemetasaun')
	activity = models.TextField( verbose_name='Deskridsaun Actividade')
	amount_of_funds =models.CharField(max_length=300, null=True,verbose_name='Montante Orcamento')
	Funder = models.CharField(max_length = 300, verbose_name='Funder')
	contact_person = models.CharField(max_length = 300, verbose_name='Contact Person', blank=True)
	

	class Meta:
		verbose_name = 'activity'
		verbose_name_plural = 'activities'
		ordering = ['-date']

	def __str__(self):
		return self.activity

class Report(models.Model):
	report = models.CharField("Anual Report", max_length=50, null=True)
	years=models.ForeignKey(Year, on_delete=models.CASCADE, related_name='get_years', verbose_name='Tinan')
	# naran_folder = models.CharField("Naran Folder", max_length=50, null=True)
	upload_file = models.FileField(upload_to='FilePdf/', null=True, blank=True, verbose_name="Dokumen PDF", help_text="Upload file PDF")



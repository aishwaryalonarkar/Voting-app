from django.db import models

# Create your models here.
class Party(models.Model):
	party_name = models.CharField(max_length=200, default=None)
	date_of_est = models.DateField('date')
	moto = models.CharField(max_length=400, default=None)
	party_leader = models.CharField(max_length=200,default=None)
	founded_by = models.CharField(max_length=200,default=None)
	party_logo_name = models.CharField(max_length=200,default=None)
	no_of_votes = models.IntegerField(default=0)
	party_logo = models.ImageField(upload_to='image', blank=True, null=True,default='../media/image/abc.jpg') 
	leader = models.ImageField(upload_to='image', blank=True, null=True,default='../media/image/abcd.jpg')
	def __str__(self):
		return self.party_name

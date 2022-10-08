from django.db import models

# Create your models here.

class studentModel(models.Model):
	
	Name = models.CharField(max_length = 30,null = True)
	Roll_no = models.IntegerField(null = True)
	Address = models.TextField()
	
	def __str__(self):
		return "{} {} {} {}".format(self.id,self.Name,self.Roll_no,self.Address)

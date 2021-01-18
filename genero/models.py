from django.db import models
from django.forms import ModelForm

# Create your models here.
class Genero(models.Model):
	descricao = models.CharField(max_length=100)

	def __str__(self):
		return self.descricao

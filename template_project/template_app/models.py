from django.db import models

# Create your models here.

class Mensaje(models.Model):

	mensaje = models.CharField(max_length=240)

	class Meta():
		db_table = 'mensajes'
		
	'''
	def __str__(self):
		return str(self.attr1) + ' - ' + str(self.attr2)
	'''


class Post(models.Model):

	autor = models.CharField(max_length=100, default="Anonymous")
	titulo = models.CharField(max_length=100)
	imagen = models.FileField(upload_to='template_project/static/uploads/')
	text = models.CharField(max_length=240)

	class Meta():
		db_table = 'posts'
		
	'''
	def __str__(self):
		return str(self.attr1) + ' - ' + str(self.attr2)

	'''


class Seguidos(models.Model):

	seguidor = models.CharField(max_length=100)
	seguido = models.CharField(max_length=100)

	class Meta():
		db_table = 'seguidos'
		
	'''
	def __str__(self):
		return str(self.attr1) + ' - ' + str(self.attr2)
	'''


class Likes(models.Model):

	idPost = models.CharField(max_length=100)
	seguidor = models.CharField(max_length=100)

	class Meta():
		db_table = 'likes'
		
	'''
	def __str__(self):
		return str(self.attr1) + ' - ' + str(self.attr2)
	'''
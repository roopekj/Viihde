from django.db import models

class URL(models.Model):
	query = models.CharField(max_length=64)
	url = models.CharField(max_length=256)

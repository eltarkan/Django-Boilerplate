from django.db import models


class Cars(models.Model):
    brand = models.CharField(max_length=20)
    year = models.DateTimeField(auto_now_add=True)

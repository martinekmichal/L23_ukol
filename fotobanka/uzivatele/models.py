from django.db import models


class Data(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    cena = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

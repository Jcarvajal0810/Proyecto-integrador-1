from django.db import models

class News(models.Model):
    # Tus campos van aquí, por ejemplo:
    headline = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField()

    def __str__(self): return self.headline

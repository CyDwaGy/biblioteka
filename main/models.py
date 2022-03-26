from django.db import models

class Book(models.Model):
    tytuł = models.CharField(max_length=200)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    zdjęcie = models.ImageField(upload_to="main/static/main/images/")

    def __str__(self):
        return self.tytuł

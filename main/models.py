from django.db import models


class Book(models.Model):
    tytuł = models.CharField(max_length=200)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    zdjęcie = models.ImageField(upload_to=f'books_covers/')
    opis = models.TextField()
    autor = models.CharField(max_length=200)
    data_publikacji = models.DateField(null=True)

    def __str__(self):
        return self.tytuł

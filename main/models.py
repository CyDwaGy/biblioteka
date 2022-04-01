from django.db import models
from django.conf import settings


class Book(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    picture = models.ImageField(upload_to=f'books_covers/', blank=True)
    desc = models.TextField()
    author = models.CharField(max_length=200)
    pub_date = models.DateField()

    def __str__(self):
        return self.title

class ItemOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Book, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.item.title

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(ItemOrder, null=True)
    ordered = models.BooleanField(default=False)
    order_date = models.DateField(null=True)

    def __str__(self):
        return self.user.username



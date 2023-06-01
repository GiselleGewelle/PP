from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.title}'


class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    description = models.TextField(blank=True, null=True)


    def __str__(self) -> str:
        return f'{self.title}'


# ./manage.py shell
# from main.models import Product, Category
# a = Product.objects.all()
# b = Category.objects.all()
# c = b[2]
# b = [x for x in c.category.all()]

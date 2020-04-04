from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'sub_categories'

    def __str__(self):
        return self.name

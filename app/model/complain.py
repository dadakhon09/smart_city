from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

from app.model.category import Category, SubCategory

STATUS = [
    (0, 'Pending'),
    (1, 'Accepted'),
    (2, 'Rejected'),
    (3, 'Solved'),
]


class Complain(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category_id = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to='complains')
    status = models.IntegerField(choices=STATUS, default=0)
    comment = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'complains'

    def __str__(self):
        return self.id


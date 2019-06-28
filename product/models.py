from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class Category(models.Model):
    STATUS = (
        (1, 'True'),
        (2, 'False')
    )
    parent_id = models.IntegerField()
    title = models.CharField(max_length=130, blank=True)
    key = models.CharField(max_length=130, blank=True)
    description = models.CharField(max_length=130, blank=True)
    image = models.ImageField()
    status = models.IntegerField(choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_At = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    STATUS = (
        (1, 'True'),
        (2, 'False')
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    parent_id = models.IntegerField()
    title = models.CharField(max_length=130, blank=True)
    key = models.CharField(max_length=130, blank=True)
    description = models.CharField(max_length=130, blank=True)
    price = models.FloatField()
    amount = models.IntegerField()
    detail = RichTextUploadingField(blank=True)
    image = models.ImageField(upload_to='images')
    status = models.IntegerField(choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_At = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

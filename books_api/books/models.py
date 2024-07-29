from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField()
    isbn = models.CharField(max_length=25, unique=True)
    pages = models.IntegerField()
    cover = models.ImageField(upload_to='covers/')

    def __str__(self):
        return self.title

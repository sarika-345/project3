from django.db import models

class Film(models.Model):
    cover=models.ImageField(upload_to='film/img', null=True, blank=True)
    title=models.CharField(max_length=30)
    desc=models.CharField(max_length=100)
    name=models.CharField(max_length=30)
    date=models.IntegerField()
    rating=models.IntegerField()

    def __str__(self):
        return self.title

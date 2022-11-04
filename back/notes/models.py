from django.db import models

# Create your models here.
class Note(models.Model):
    id = models.IntegerField(primary_key = True)
    content = models.TextField()
    name = models.CharField(max_length = 80, blank = True)
    price = models.IntegerField(default = '0', blank = True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}:{self.price}"

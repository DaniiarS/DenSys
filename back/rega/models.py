from django.db import models

# Create your models here.
class ItemModel(models.Model):
    inn = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 80, blank = False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.iin}"

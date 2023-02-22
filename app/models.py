from django.db import models

# Create your models here.

class Profile(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return self.name

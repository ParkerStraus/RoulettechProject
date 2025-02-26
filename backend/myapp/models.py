from django.db import models

class Contact(models.Model):
    id = models.AutoField(primary_key=True)  # Automatically increments
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


from django.db import models

# Create your models here.
class CSVData(models.Model):
    id = models.IntegerField(unique=True,primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    profession = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id) + "," + self.firstname + "," + self.lastname + "," + self.email + "," + self.password + "," + self.profession
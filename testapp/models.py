from django.db import models

# Create your models here.
class names(models.Model):
    name=models.CharField( max_length=50)


    def __str__(self):
       return self.name

class Language(models.Model):
    title = models.CharField(max_length=56)

    def __str__(self):
        return self.title


class Entry(models.Model):
    name = models.ForeignKey('names', on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name="Favourite Language")

    def __str__(self):
        return self.name.name




class Events(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.name        
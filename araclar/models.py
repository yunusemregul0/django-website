from django.db import models
from django.utils.text import slugify


class marka(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(default="", null=False,unique=True,db_index=True, max_length=50)

    def __str__(self):
        return f"{self.name}"

class araclar(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="images",default="")
    date= models.DateField(auto_now=True)
    isActive = models.BooleanField(default=False)
    isHome = models.BooleanField(default=False)
    slug = models.SlugField(default="",blank=True,null=False, unique=True, db_index=True) 
    marka = models.ManyToManyField(marka)

    def __str__(self):
        return f"{self.title}"

class UploadModel(models.Model):
    image = models.ImageField(upload_to="images")




from django.db import models

class Demo_Models(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(null=True)
    profile_pic = models.FileField(upload_to='prof_pic/',max_length=250,null=True)

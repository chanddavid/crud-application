from django.contrib.auth.models import User
from django.db import models


class ModelName(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()


# class ModelName2(models.Model):
#     username=models.CharField(max_length=20)
#     password=models.CharField(max_length=20)
#     re_enterpassword=models.CharField(ma  x_length=20)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.user.username

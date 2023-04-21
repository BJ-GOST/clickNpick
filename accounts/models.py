from django.contrib.auth.models import AbstractUser
from django.db import models

class Reader(AbstractUser):
    shopname = models.CharField(max_length=255, null=True, blank=True)


{
"username":"Billy",
"email":"billyilla@gmail.com",
"password":"744b44jl",
"shopname":"myshop"
}
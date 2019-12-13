from django.db import models
from django.core.validators import MinValueValidator


class UserModel(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    contact = models.CharField(max_length=10)
    email = models.EmailField(max_length=120)
    password = models.CharField(max_length=50)
    # PositiveIntegerField rakhda ni huncha models.PositiveIntegerField(validators=[MinValue_validator(0)])
    reputation = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return(self.name)

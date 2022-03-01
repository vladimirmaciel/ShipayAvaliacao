from django.db import models
from datetime import datetime


class Claims(models.Model):
    descricao = models.CharField(max_length=100)
    ativo = models.BooleanField()

    def __str__(self):
        return self.descricao


class Roles(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Users(models.Model):

    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    description = models.ManyToManyField(Claims, blank=True, null=True)
    password = models.CharField(max_length=10, blank=True, null=True)
    role = models.ForeignKey(
        Roles, on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "%s (%s)" % (
            self.name,
            ", ".join(
                description.descricao for description in self.description.all()),
        )

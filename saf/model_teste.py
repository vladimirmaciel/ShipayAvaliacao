from django.db import models

# Create your models here.


class Claims(models.Model):

    description = models.CharField(max_length=100)
    active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'claims'


class Roles(models.Model):

    description = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'roles'


class Users(models.Model):

    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    description = models.ManyToManyField(Claims)
    password = models.CharField(max_length=10)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    created_at = models.DateField()
    updated_at = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

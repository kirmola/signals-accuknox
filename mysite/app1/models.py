from django.db import models

# Create your models here.


class TestModel1(models.Model):
    name = models.CharField(max_length=100)

class TestModel2(models.Model):
    name = models.CharField(max_length=100)

class TestModel3(models.Model):
    name = models.CharField(max_length=100)
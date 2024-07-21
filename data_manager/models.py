from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    domain = models.CharField(max_length=255, blank=True, null=True)
    year_founded = models.CharField(max_length=255,blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    size_range = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    linkedin_url = models.URLField()
    current_employee_estimate = models.CharField(max_length=255, blank=True, null=True)
    total_employee_estimate = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name


class DataFile(models.Model):
    file = models.FileField(upload_to='files')


class Industry(models.Model):
    industry = models.CharField(max_length=255)


class YearFounded(models.Model):
    year_founded = models.CharField(max_length=255)


class City(models.Model):
    city = models.CharField(max_length=255)


class State(models.Model):
    state = models.CharField(max_length=255)


class Country(models.Model):
    country = models.CharField(max_length=255)



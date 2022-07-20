from django.db import models
from django.urls import reverse


class Company(models.Model):
    name = models.CharField(max_length=355)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('emails:all-recipients')


class Position(models.Model):
    name = models.CharField(max_length=355)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('emails:all-recipients')


class Recipient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.ManyToManyField(Position)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('emails:all-recipients')

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse










class Card(models.Model):
    Card_num = models.IntegerField()
    Name = models.CharField(max_length=200)
    Card_data = models.CharField(max_length=11)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,

    )

    def __str__(self):
        return self.Name


    def get_absolute_url(self):
        return reverse('code')


class code(models.Model):
    card_num = models.CharField(max_length=4)
    cod = models.CharField(max_length=7)

    def __str__(self):
        return self.card_num


    def get_absolute_url(self):
        return reverse('home')
from django.db import models
from django.utils import timezone


# Create your models here.


class ToDoList(models.Model):

    baslik = models.CharField(max_length=144,verbose_name="Name")
    aciklama = models.TextField(blank=True,null=True,verbose_name="Description")
    eklenme_tarihi = models.DateTimeField(default=timezone.now,verbose_name="Deadline")
    durum = models.BooleanField(default=False,verbose_name="Status")



    def __str__(self):
        return self.baslik
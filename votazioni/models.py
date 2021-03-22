from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class CandidatiUomo(models.Model):
     nome_e_cognome = models.CharField(max_length=255)
     votes = models.IntegerField(default=0, )

     class Meta:
         verbose_name = "Candidato uomo"
         verbose_name_plural = "Candidati uomo"

     def __str__(self):
         return self.nome_e_cognome


class CandidatiDonna(models.Model):
    nome_e_cognome = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Candidato donna"
        verbose_name_plural = "Candidate donna"

    def __str__(self):
        return self.nome_e_cognome


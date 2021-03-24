from django.db import models

# Create your models here.

from django.db import models



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



#in models.py
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Votes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ha_votato=models.BooleanField(default=False)
    #other fields here

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            profile, created = Votes.objects.get_or_create(user=instance)

    post_save.connect(create_user_profile, sender=User)



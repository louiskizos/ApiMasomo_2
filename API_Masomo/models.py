from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Etablissement(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='images/')
    designationEcole = models.CharField(max_length=150)
    arreteMin = models.CharField(max_length=100)
    adresse = models.TextField()
    telephone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    typesEcole = models.CharField(max_length=100)  # PRIVEE ou PUBLIQUE
    degree = models.CharField(max_length=100)  # PRIMAIRE ou SECONDAIRE
    promoteur = models.CharField(max_length=100)
    biographie = models.TextField()
    
    def __str__(self):
        return self.designationEcole

class MasomoClasse(models.Model):
    etablissement = models.ForeignKey(Etablissement, null=True, on_delete=models.SET_NULL)
    designationClasse = models.CharField(max_length=150)

    def __str__(self):
        return self.designationClasse

class MasomoSection(models.Model):
    classeMasomo = models.ForeignKey(MasomoClasse, null=True, on_delete=models.SET_NULL)
    designationSection = models.CharField(max_length=150)

    def __str__(self):
        return self.designationSection

class MasomoOption(models.Model):
    sectionMasomo = models.ForeignKey(MasomoSection, null=True, on_delete=models.SET_NULL)
    designationOption = models.CharField(max_length=200)

    def __str__(self):
        return self.designationOption

from django.db import models

from accounts.models import Enqueteur


# Create your models here.
class Arrondissement(models.Model):
    IdArrondissement = models.IntegerField(unique=True)
    nomArrondissement = models.CharField(max_length=25)


class ZD(models.Model):
    numZD = models.IntegerField(unique=True)
    numGrappe = models.IntegerField(unique=True)
    nomBloc = models.CharField(max_length=25)
    arrondissement = models.ForeignKey(Arrondissement, on_delete=models.PROTECT)


class Structure(models.Model):
    numStructure = models.IntegerField(unique=True)
    description = models.CharField(max_length=100)
    usage = models.CharField(max_length=100)
    type = models.CharField(max_length=25)
    zd = models.ForeignKey(ZD, on_delete=models.PROTECT)


class Menage(models.Model):
    numMenage = models.IntegerField(unique=True)
    nomChefDuMenage = models.CharField(max_length=75)
    observation = models.CharField(max_length=250)
    structure = models.ForeignKey(Structure, on_delete=models.PROTECT)


class Charger(models.Model):
    codeEnqueteur = models.ForeignKey(Enqueteur, null=True, on_delete=models.SET_NULL)
    numMenage = models.ForeignKey(Menage, null=True, on_delete=models.SET_NULL)


class Effectuer(models.Model):
    codeEnqueteur = models.ForeignKey(Enqueteur, null=True, on_delete=models.SET_NULL)
    numMenage = models.ForeignKey(Menage, null=True, on_delete=models.SET_NULL)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()

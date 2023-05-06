from django.db import models

class Yonalish(models.Model):
    nom = models.CharField(max_length=70)
    aktiv = models.BooleanField(null=True,default=False)

class Fan(models.Model):
    nom = models.CharField(max_length=50)
    yonalish = models.ForeignKey(Yonalish,on_delete=models.CASCADE)
    asosiy = models.BooleanField(verbose_name="Asosiy fan yoki yoq?",default=False)

class Ustoz(models.Model):
    tanlov = [("Erkak","Erkak"),("Ayol","Ayol")]
    ism = models.CharField(max_length=35)
    jins = models.CharField(max_length=10,choices=tanlov)
    yosh = models.PositiveSmallIntegerField()
    daraja =models.CharField(max_length=50,verbose_name="Masalan Bakalavr yoki Magistr")
    fan = models.ForeignKey(Fan,on_delete=models.CASCADE)

from django.db import models
from website.models import Base


class Categorie(Base):
    
    nom = models.CharField(max_length=255)
    desc_categorie = models.TextField()
    icon = models.FileField(upload_to='images', null=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

class Agence(Base):
    
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Agence'
        verbose_name_plural = 'Agences'

class Service(Base):
    
    titre = models.CharField(max_length=255)
    description = models.TextField()
    image = models.FileField(upload_to='images')
    prix = models.FloatField(default=0)
    periode = models.CharField(max_length=255)
    detail = models.CharField(max_length=255)
    lit = models.CharField(max_length=255)
    sale_de_bain = models.CharField(max_length=255)
    categorie = models.ForeignKey("service.Categorie",related_name= 'categorieservice', on_delete=models.CASCADE , null=True)
    agence = models.ForeignKey("service.Agence",related_name= 'agenceservice', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

class Nmb_annonce(Base):
    
    semaine = models.IntegerField(default=0)
    mois = models.IntegerField(default=0)
    annee = models.IntegerField(default=0)


    def __str__(self):
        return self.semaine

    class Meta:
        verbose_name = 'Nmb_annonce'
        verbose_name_plural = 'Nmb_annonces'


class Contact(Base):
    CHOIX = (
        ('A', 'Appartements'),
        ('C', 'Car'),
        ('S', 'Shopping'),
        ('F', 'Food & Life'),
        ('T', 'Traveling'),
    )
    nom = models.IntegerField(default=0)
    prenom = models.IntegerField(default=0)
    email = models.IntegerField(default=0)
    choix = models.CharField(max_length=50 , choices=CHOIX)
    message = models.TextField()
    


    def __str__(self):
        return self.semaine

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
# Create your models here.
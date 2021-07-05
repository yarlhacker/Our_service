from django.db import models


class Base(models.Model):

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Banner(Base):
    
    titre = models.CharField(max_length=255)
    image = models.FileField(upload_to='images')

    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'



class Website(Base):
    
    adresse = models.CharField(max_length=255 , null=True)
    mapp = models.TextField()
    phone= models.CharField(max_length=255)
    logo_site = models.FileField(upload_to='images')
    logo_site_footer = models.FileField(upload_to='images' , null=True)
    nom_site = models.CharField(max_length=255)
    titre_categorie = models.CharField(max_length=255)
    titre_contact = models.CharField(max_length=255)
    titre_listing = models.CharField(max_length=255)

    def __str__(self):
        return self.nom_site

    class Meta:
        verbose_name = 'Website'
        verbose_name_plural = 'Websites'


class Configuration(Base):
    
    desc_categorie = models.TextField()
    desc_contact = models.TextField()
    desc_listing = models.TextField()
    desc_footer = models.TextField()
    copyrights = models.TextField()

    class Meta:
        verbose_name = 'Configuration'
        verbose_name_plural = 'Configurations'

class Lienutil(Base):
    
    nom = models.CharField(max_length=250)
    lien = models.URLField(max_length=200)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Lien_util'
        verbose_name_plural = 'Lien_utils'


class social(Base):
    
    nom = models.CharField(max_length=250)
    lien = models.URLField(max_length=200)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'social'
        verbose_name_plural = 'sociaux'

# Create your models here.

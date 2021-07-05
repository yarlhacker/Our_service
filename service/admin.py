from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    # Liste des champs a afficher
    list_display = ('nom','date_add', 'date_update', 'status')

    list_editable = ('status',)


@admin.register(models.Agence)
class AgenceAdmin(admin.ModelAdmin):
    # Liste des champs a afficher
    list_display = ('nom','date_add', 'date_update', 'status')

    list_editable = ('status',)

@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    # Liste des champs a afficher
    list_display = ('images_view','titre','prix','date_add', 'date_update', 'status')

    list_editable = ('status',)

    def images_view(self, obj):
        if obj:
            return mark_safe(f'<img src="{obj.image.url}" style="height:50px; width:100px">')
        else:
            return '_'
    images_view.short_description = 'Aperçu des images'



@admin.register(models.Nmb_annonce)
class Nmb_annonceAdmin(admin.ModelAdmin):
    # Liste des champs a afficher
    list_display = ('semaine','mois','annee','date_add', 'date_update', 'status')

    list_editable = ('status',)

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    # Liste des champs a afficher
    list_display = ('nom','prenom','date_add', 'date_update', 'status')

    list_editable = ('status',)
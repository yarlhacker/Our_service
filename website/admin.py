from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
    # Liste des champs a afficher
    list_display = ('images_view','titre','date_add', 'date_update', 'status')

    list_editable = ('status',)

    def images_view(self, obj):
                
        if obj:
            return mark_safe(f'<img src="{obj.image.url}" style="height:50px; width:100px">')
        else:
            return '_'
    images_view.short_description = 'Aperçu des images'



@admin.register(models.Website)
class WebsiteAdmin(admin.ModelAdmin):

    # Liste des champs a afficher
    list_display = ('images_view','phone','nom_site','date_add', 'date_update', 'status')

    list_editable = ('status',)

    def images_view(self, obj):
                
        if obj:
            return mark_safe(f'<img src="{obj.logo_site.url}" style="height:50px; width:100px">')
        else:
            return '_'
    images_view.short_description = 'Aperçu des images'




@admin.register(models.Configuration)
class ConfigurationAdmin(admin.ModelAdmin):

    # Liste des champs a afficher
    list_display = ('copyrights','date_add', 'date_update', 'status')

    list_editable = ('status',)



@admin.register(models.social)
class socialAdmin(admin.ModelAdmin):

    # Liste des champs a afficher
    list_display = ('nom','date_add', 'date_update', 'status')

    list_editable = ('status',)



@admin.register(models.Lienutil)
class LienutilAdmin(admin.ModelAdmin):

    # Liste des champs a afficher
    list_display = ('nom','date_add', 'date_update', 'status')

    list_editable = ('status',)

# Register your models here.

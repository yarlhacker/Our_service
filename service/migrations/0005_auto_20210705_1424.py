# Generated by Django 3.2.5 on 2021-07-05 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_alter_service_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='agence',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agenceservice', to='service.agence'),
        ),
        migrations.AddField(
            model_name='service',
            name='categorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categorieservice', to='service.categorie'),
        ),
    ]
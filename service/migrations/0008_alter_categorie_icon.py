# Generated by Django 3.2.5 on 2021-07-05 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_categorie_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='icon',
            field=models.FileField(null=True, upload_to='images'),
        ),
    ]

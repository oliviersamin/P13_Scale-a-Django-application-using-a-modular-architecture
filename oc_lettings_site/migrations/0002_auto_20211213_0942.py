# Generated by Django 3.0 on 2021-12-13 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Adresse', 'verbose_name_plural': 'Adresses'},
        ),
        migrations.AlterModelOptions(
            name='letting',
            options={'verbose_name': 'Location', 'verbose_name_plural': 'Locations'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Profil', 'verbose_name_plural': 'Profils'},
        ),
    ]

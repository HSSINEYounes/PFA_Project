# Generated by Django 4.2.1 on 2023-05-16 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_remove_etudiant_father_remove_etudiant_filiere_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Filiere',
        ),
    ]

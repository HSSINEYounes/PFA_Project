# Generated by Django 4.2.1 on 2023-05-16 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_delete_filiere'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomCour', models.CharField(max_length=30)),
                ('heureDebut', models.TimeField()),
                ('heureFin', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=10)),
                ('prenom', models.CharField(max_length=10)),
                ('genre', models.CharField(max_length=2)),
                ('email', models.CharField(max_length=20)),
                ('telephone', models.CharField(max_length=15)),
                ('groupe', models.CharField(max_length=3)),
                ('niveau', models.CharField(max_length=15)),
                ('father', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.parent')),
            ],
        ),
        migrations.CreateModel(
            name='Filiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeF', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomSalle', models.CharField(max_length=4)),
                ('etage', models.IntegerField()),
                ('TypeSalle', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Salle_Cour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_cour', models.DateField()),
                ('cour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.cour')),
                ('salle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.salle')),
            ],
        ),
        migrations.CreateModel(
            name='Presence_Cour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_presence', models.DateField()),
                ('cour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.cour')),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.etudiant')),
            ],
        ),
        migrations.AddField(
            model_name='etudiant',
            name='filiere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.filiere'),
        ),
    ]

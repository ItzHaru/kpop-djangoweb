# Generated by Django 4.2 on 2023-06-13 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_skupina_fotka'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='spolecnost',
            options={'ordering': ['nazev_spolecnosti'], 'verbose_name': 'Spolecnost', 'verbose_name_plural': 'Spolecnosti'},
        ),
    ]

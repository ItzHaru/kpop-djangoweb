# Generated by Django 4.2 on 2023-05-12 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_ceo_pohlavi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skupina',
            name='zkratka_nazev',
            field=models.CharField(blank=True, help_text='Zadej zkratku názvu', max_length=10, null=True, verbose_name='Zkratka názvu'),
        ),
    ]

# Generated by Django 4.2 on 2023-06-14 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_spolecnost_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='spolecnost',
            name='logo',
            field=models.ImageField(blank=True, help_text='Nahrajte logo spolecnosti', null=True, upload_to='spolecnosti', verbose_name='Logo spolecnosti'),
        ),
    ]

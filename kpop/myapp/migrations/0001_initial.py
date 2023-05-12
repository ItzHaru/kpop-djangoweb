# Generated by Django 4.2 on 2023-05-12 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ceo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeno', models.CharField(error_messages={'blank': 'Jméno CEO musí být vyplněno'}, help_text='Zadejte jméno CEO', max_length=50, verbose_name='Jméno CEO')),
                ('prijmeni', models.CharField(error_messages={'blank': 'Příjmení CEO musí být vyplněno'}, help_text='Zadejte příjmení CEO', max_length=50, verbose_name='Příjmení CEO')),
                ('datum_narozeni', models.DateField(blank=True, null=True, verbose_name='Datum narození')),
                ('pohlavi', models.CharField(choices=[('muž', 'm'), ('žena', 'ž')], help_text='Vyberte pohlaví', max_length=10, verbose_name='Pohlaví')),
            ],
            options={
                'verbose_name': 'CEO',
                'verbose_name_plural': 'CEOs',
                'ordering': ['prijmeni', 'jmeno'],
            },
        ),
        migrations.CreateModel(
            name='Zanry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev_zanru', models.CharField(help_text='Zadej název žánr', max_length=50, unique=True, verbose_name='Žánry')),
            ],
            options={
                'verbose_name': 'Žánr',
                'verbose_name_plural': 'Žánry',
                'ordering': ['nazev_zanru'],
            },
        ),
        migrations.CreateModel(
            name='Spolecnost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev_spolecnosti', models.CharField(error_messages={'blank': 'Jméno společnosti musí být vyplněno'}, help_text='Zadejte název společnosti', max_length=50, verbose_name='Název společnosti')),
                ('datum_zalozeni', models.DateField(blank=True, null=True, verbose_name='Datum založení')),
                ('hlavni_sidlo', models.CharField(blank=True, help_text='Zadej hlavní sídlo', max_length=100, null=True, verbose_name='Hlavní sídlo')),
                ('ceo', models.ForeignKey(default=0, help_text='Vyber CEO', on_delete=django.db.models.deletion.CASCADE, to='myapp.ceo', verbose_name='Jméno CEO')),
            ],
            options={
                'verbose_name': 'Společnost',
                'verbose_name_plural': 'Společnosti',
                'ordering': ['nazev_spolecnosti'],
            },
        ),
        migrations.CreateModel(
            name='Skupina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev_skupiny', models.CharField(error_messages={'blank': 'Jméno skupiny musí být vyplněno'}, help_text='Zadejte název skupiny', max_length=50, verbose_name='Název skupiny')),
                ('zkratka_nazev', models.CharField(help_text='Zadej zkratku názvu', max_length=10, null=True, verbose_name='Zkratka názvu')),
                ('debut', models.DateField(blank=True, null=True, verbose_name='Datum debutu')),
                ('spolecnost', models.ForeignKey(default=0, help_text='Vyber společnost', on_delete=django.db.models.deletion.CASCADE, to='myapp.spolecnost', verbose_name='Společnost')),
                ('zanr', models.ManyToManyField(help_text='Vyberte žánry', to='myapp.zanry', verbose_name='Žánry')),
            ],
            options={
                'verbose_name': 'Skupina',
                'verbose_name_plural': 'Skupiny',
                'ordering': ['nazev_skupiny'],
            },
        ),
        migrations.CreateModel(
            name='Clen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeno', models.CharField(error_messages={'blank': 'Jméno člena musí být vyplněno'}, help_text='Zadejte jméno člena', max_length=50, verbose_name='Jméno člena')),
                ('prijmeni', models.CharField(error_messages={'blank': 'Příjmení člena musí být vyplněno'}, help_text='Zadejte příjmení člena', max_length=50, verbose_name='Příjmení člena')),
                ('pseudonym', models.CharField(help_text='Zadejte pseudonym člena', max_length=50, verbose_name='Pseudonym člena')),
                ('datum_narozeni', models.DateField(blank=True, null=True, verbose_name='Datum narození')),
                ('pohlavi', models.CharField(choices=[('muž', 'Muž'), ('žena', 'Žena')], help_text='Vyberte pohlaví člena', max_length=10, verbose_name='Pohlaví člena')),
                ('znameni', models.CharField(choices=[('beran', 'Beran'), ('býk', 'Býk'), ('blíženci', 'Blíženci'), ('rak', 'Rak'), ('lev', 'Lev'), ('panna', 'Panna'), ('váhy', 'Váhy'), ('štír', 'Štír'), ('střelec', 'Střelec'), ('kozoroh', 'Kozoroh'), ('vodnář', 'Vodnář'), ('ryby', 'Ryby')], help_text='Vyberte znamení člena', max_length=10, verbose_name='Znamení člena')),
                ('vyska', models.PositiveIntegerField(help_text='Zadejte výšku člena', verbose_name='Výška člena')),
                ('skupina', models.ForeignKey(default=0, help_text='Vyber skupinu', on_delete=django.db.models.deletion.CASCADE, to='myapp.skupina', verbose_name='Skupina')),
            ],
            options={
                'verbose_name': 'Člen',
                'verbose_name_plural': 'Členové',
                'ordering': ['prijmeni', 'jmeno'],
            },
        ),
    ]

from django.db import models

# Create your models here.
class Spolecnost(models.Model):
    nazev_spolecnosti = models.CharField(max_length=50, verbose_name='Název společnosti', help_text='Zadejte název společnosti',
                                        error_messages={'blank': 'Jméno společnosti musí být vyplněno'}, null=False, blank=False)
    datum_zalozeni = models.DateField(blank=True, null=True, verbose_name='Datum založení', auto_now=False, auto_now_add=False)
    hlavni_sidlo = models.CharField(max_length=100, verbose_name='Hlavní sídlo', help_text='Zadej hlavní sídlo', blank=True, null=True)
    ceo = models.ForeignKey('Ceo', on_delete=models.CASCADE, verbose_name='Jméno CEO', help_text='Vyber CEO', default=0)
    logo = models.ImageField(upload_to='spolecnosti', null=True, blank=True, verbose_name='Logo spolecnosti',
                              help_text='Nahrajte logo spolecnosti')

    class Meta:
        ordering = ['nazev_spolecnosti']
        verbose_name = 'Spolecnost'
        verbose_name_plural = 'Spolecnosti'

    def __str__(self):
        return self.nazev_spolecnosti
class Ceo(models.Model):
    POHLAVI_VYBER = [
        ("muž", "Muž"),
        ("žena", "Žena")
    ]

    jmeno = models.CharField(max_length=50, verbose_name='Jméno CEO', help_text='Zadejte jméno CEO',
                             error_messages={'blank': 'Jméno CEO musí být vyplněno'}, null=False, blank=False)
    prijmeni = models.CharField(max_length=50, verbose_name='Příjmení CEO', help_text='Zadejte příjmení CEO',
                                error_messages={'blank': 'Příjmení CEO musí být vyplněno'}, null=False, blank=False)
    datum_narozeni = models.DateField(blank=True, null=True, verbose_name='Datum narození', auto_now=False, auto_now_add=False)
    pohlavi = models.CharField(max_length=10, verbose_name='Pohlaví', help_text='Vyberte pohlaví', choices=POHLAVI_VYBER)

    class Meta:
        ordering = ['prijmeni', 'jmeno']
        verbose_name = 'CEO'
        verbose_name_plural = 'CEOs'

    def __str__(self):
        return f'{self.jmeno} {self.prijmeni}'

class Zanry(models.Model):
    nazev_zanru = models.CharField(max_length=50, verbose_name='Žánry', help_text='Zadej název žánr', unique=True)
    class Meta:
        ordering = ['nazev_zanru']
        verbose_name = 'Žánr'
        verbose_name_plural = 'Žánry'

    def __str__(self):
        return f'{self.nazev_zanru}'
class Skupina(models.Model):
    nazev_skupiny = models.CharField(max_length=50, verbose_name='Název skupiny', help_text='Zadejte název skupiny',
                                        error_messages={'blank': 'Jméno skupiny musí být vyplněno'}, null=False, blank=False)
    zkratka_nazev = models.CharField(max_length=10, verbose_name='Zkratka názvu', help_text='Zadej zkratku názvu', null=True, blank=True)
    debut = models.DateField(blank=True, null=True, verbose_name='Datum debutu', auto_now=False, auto_now_add=False)
    zanr = models.ManyToManyField('Zanry', verbose_name='Žánry', help_text='Vyberte žánry')
    spolecnost = models.ForeignKey('Spolecnost', on_delete=models.CASCADE, verbose_name='Společnost', help_text='Vyber společnost', default=0)
    fotka = models.ImageField(upload_to='skupiny', null=True, blank=True, verbose_name='Fotka kpop skupiny', help_text='Nahrajte fotku skupiny')
    class Meta:
        ordering = ['nazev_skupiny']
        verbose_name = 'Skupina'
        verbose_name_plural = 'Skupiny'

    def __str__(self):
        return self.nazev_skupiny

class Clen(models.Model):
    POHLAVI_VYBER = [
        ("muž", "Muž"),
        ("žena", "Žena")
    ]

    ZNAMENI_VYBER = [
        ("beran", "Beran"),
        ("býk", "Býk"),
        ("blíženci", "Blíženci"),
        ("rak", "Rak"),
        ("lev", "Lev"),
        ("panna", "Panna"),
        ("váhy", "Váhy"),
        ("štír", "Štír"),
        ("střelec", "Střelec"),
        ("kozoroh", "Kozoroh"),
        ("vodnář", "Vodnář"),
        ("ryby", "Ryby")
    ]

    jmeno = models.CharField(max_length=50, verbose_name='Jméno člena', help_text='Zadejte jméno člena',
                             error_messages={'blank': 'Jméno člena musí být vyplněno'}, null=False, blank=False)
    prijmeni = models.CharField(max_length=50, verbose_name='Příjmení člena', help_text='Zadejte příjmení člena',
                                error_messages={'blank': 'Příjmení člena musí být vyplněno'}, null=False, blank=False)
    pseudonym = models.CharField(max_length=50, verbose_name='Pseudonym člena', help_text='Zadejte pseudonym člena', null=False, blank=False)
    datum_narozeni = models.DateField(blank=True, null=True, verbose_name='Datum narození')
    pohlavi = models.CharField(max_length=10, verbose_name='Pohlaví člena', help_text='Vyberte pohlaví člena', choices=POHLAVI_VYBER, null=False, blank=False)
    znameni = models.CharField(max_length=10, verbose_name='Znamení člena', help_text='Vyberte znamení člena', choices=ZNAMENI_VYBER)
    vyska = models.PositiveIntegerField(verbose_name='Výška člena', help_text='Zadejte výšku člena')
    skupina = models.ForeignKey('Skupina', on_delete=models.CASCADE, verbose_name='Skupina', help_text='Vyber skupinu', default=0)

    class Meta:
        ordering = ['prijmeni', 'jmeno']
        verbose_name = 'Clen'
        verbose_name_plural = 'Clenové'

    def __str__(self):
        return f'{self.jmeno, self.prijmeni}'

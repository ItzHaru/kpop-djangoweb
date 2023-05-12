from django.contrib import admin
from .models import Spolecnost, Ceo, Zanry, Skupina, Clen

# Register your models here.
admin.site.register(Spolecnost)
admin.site.register(Ceo)
admin.site.register(Zanry)
admin.site.register(Skupina)
admin.site.register(Clen)
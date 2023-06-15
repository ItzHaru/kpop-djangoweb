from django.shortcuts import render
from django.views.generic import DetailView

from.models import Skupina, Spolecnost

def index(request):
    skupina = 'skupiny'
    context = {
        'nazev': skupina,
        'skupiny': Skupina.objects.order_by('nazev_skupiny'),
        'spolecnosti': Spolecnost.objects.all()
    }
    return render(request, 'index.html', context=context)

def skupiny(request):
    context = {
        'skupiny': Skupina.objects.all(),
    }
    return render(request, 'skupiny.html', context=context)

def spolecnosti(request):
    context = {
        'spolecnosti': Spolecnost.objects.all()
    }
    return render(request, 'spolecnosti.html', context=context)

class SkupinaDetailView(DetailView):
    model = Skupina
    template_name = 'skupina/detail.html'
    context_object_name = 'skupina'

class SpolecnostDetailView(DetailView):
    model = Spolecnost
    template_name = 'spolecnost/detail.html'
    context_object_name = 'spolecnost'

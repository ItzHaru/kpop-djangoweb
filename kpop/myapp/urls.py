from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('skupiny', views.skupiny, name='skupiny'),
    path('spolecnosti', views.spolecnosti, name='spolecnosti'),
    path('skupina/<int:pk>', views.SkupinaDetailView.as_view(),
         name='skupina_detail'),
    path('spolecnost/<int:pk>', views.SpolecnostDetailView.as_view(),
         name='spolecnost_detail'),
]
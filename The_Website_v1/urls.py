from django.urls import path
from .import views

app_name = "The_Website_v1"

urlpatterns=[

    path('', views.index, name ="home"),
    path('about', views.about, name ="about"),
    path('services', views.services, name ="services"),
    path('portfolio', views.portfolio, name ="portfolio"),
    path('contact/', views.contact, name ="contact"),

]
from django.urls import path
from .import views

app_name = "The_Website_v1"

urlpatterns=[

    path('', views.index, name ="home"),
    path('about', views.about, name ="about"),
    path('services', views.service, name ="services"),
    path('portfolio', views.portfolio, name ="portfolio"),
    path('contact/', views.contact, name ="contact"),
    path('project_detail/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/<int:pk>/', views.handle_url_existence, name='handle_url_existence'),
    path('blog_index/', views.PostList.as_view(), name='blog_home'),
    path('blog_index/<slug:slug>/', views.DetailView.as_view(), name='blog_detail'),


]


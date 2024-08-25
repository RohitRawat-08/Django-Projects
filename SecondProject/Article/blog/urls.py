from django.urls import path
from blog import views

urlpatterns= [
    path('',views.home, name='home'),
    path('display/<int:id>',views.display, name='display'),
]
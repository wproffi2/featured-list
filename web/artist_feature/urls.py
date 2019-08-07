from django.urls import path
from artist_feature import views

urlpatterns = [
    path('', views.index, name='index'),
]
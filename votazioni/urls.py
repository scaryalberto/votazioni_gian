from django.urls import path
from . import views


urlpatterns = [
    path('', views.votazioni, name='post_list'),
        path('voti/', views.voti, name='voti'),
]

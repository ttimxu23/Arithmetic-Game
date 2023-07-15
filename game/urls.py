from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('play', views.play, name="play"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('register', views.register, name="register"),
    path('<str:score>/<str:time>/save', views.save, name='save'),
    path('stats', views.stats, name="stats")
]
    

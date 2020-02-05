from django.urls import path
from . import views

urlpatterns = [
	path('say/', views.say, name='adventure-say'),
	path('init/', views.init, name='adenture-init'),
    path('move/', views.move, name='adventure-move'),
    path('rooms/', views.rooms, name='adventure-rooms')
]
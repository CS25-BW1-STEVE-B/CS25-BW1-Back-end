from django.urls import path
from . import views

urlpatterns = [
	path('say/', views.say, name='adventure-say'),
	path('init/', views.init.as_view(), name='adenture-init'),
    path('move/', views.move.as_view(), name='adventure-move'),
    path('rooms/', views.room.as_view(), name='adventure-rooms')
]
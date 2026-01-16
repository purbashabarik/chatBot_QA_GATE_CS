from django.urls import path
from . import views
urlpatterns =[
    path('', views.rooms, name='rooms'),
    path('pyq', views.room, name='room'),
    path('chat/', views.chat, name='chat'),
    path('room_books/', views.room_books, name='room_books'),
    path('chat_book/', views.chat_book, name='chat_book'),
]
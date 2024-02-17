from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.user_signup, name='user-signup'),
    path('login/', views.user_login, name='user-login'),
    path('notes/create/', views.note_create, name='note-create'),
    path('notes/<int:pk>/', views.note_detail, name='note-detail'),
    path('notes/', views.note_list, name='note_list'),
    # Add URL patterns for note sharing, note updates, and version history
]

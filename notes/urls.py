from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # notes
    path('notes/', views.note_list, name='note_list'),
    path('notes/create/', views.note_create, name='note_create'),
    path('notes/edit/<int:pk>/', views.note_edit, name='note_edit'),
    path('notes/delete/<int:pk>/', views.note_delete, name='note_delete'),

    # authentication
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
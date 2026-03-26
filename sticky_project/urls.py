from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # admin panel
    path('admin/', admin.site.urls),

    # notes app URLs include kar rahe hain
    path('', include('notes.urls')),
]
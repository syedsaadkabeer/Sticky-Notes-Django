from django.contrib import admin
from .models import Note

# Note model ko admin panel me register kar rahe hain
admin.site.register(Note)
from django.contrib import admin
from .models import Parvam, Story

# Register the models so they appear in the admin panel
admin.site.register(Parvam)
admin.site.register(Story)

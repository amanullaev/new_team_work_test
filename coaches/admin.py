from django.contrib import admin
from .models import TrenerModel


# Register your models here.

class TrenerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


admin.site.register(TrenerModel, TrenerAdmin)

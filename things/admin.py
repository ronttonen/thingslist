from django.contrib import admin
from things.models import Thing

class ThingAdmin(admin.ModelAdmin):
    list_display = ['title','author_email', 'last_edited']
    
admin.site.register(Thing, ThingAdmin)

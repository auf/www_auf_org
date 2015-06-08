from django.contrib import admin
from project.contacts.models import *


class ContacteAdmin(admin.ModelAdmin):

    list_display = ('nom', 'prenom', 'email', 'bureau')
    search_fields = ('bureau', 'nom')

admin.site.register(Contacte, ContacteAdmin)

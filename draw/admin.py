from django.contrib import admin
from .models import Draw
from accounts.models import Profile
# Register your models here.

class DrawAdmin(admin.ModelAdmin):
    list_display = ('user','first','second','third')
    model = Draw
    con_delete = False

admin.site.register(Draw, DrawAdmin)
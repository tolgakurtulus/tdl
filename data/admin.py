from django.contrib import admin

# Register your models here.

from .models import ToDoList

class ToDoListAdminModel(admin.ModelAdmin):

    list_display = ('baslik','eklenme_tarihi','durum')
    date_hierarchy = ('eklenme_tarihi')
    list_display_links = ('baslik','eklenme_tarihi')
    list_filter = ('baslik','eklenme_tarihi','durum')
    list_editable = ['durum']
    ordering = ['-eklenme_tarihi']
    search_fields = ['baslik', 'aciklama']

    class Meta:
        model = ToDoList

admin.site.register(ToDoList, ToDoListAdminModel)
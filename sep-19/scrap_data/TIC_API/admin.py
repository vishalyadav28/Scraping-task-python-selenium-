from django.contrib import admin
from .models import DataStore
# Register your models here.
@admin.register(DataStore)
class DataStoreAdmin(admin.ModelAdmin):
# display both name and url at model index page
    search_fields=['company_name__iexact','plan_id__exact']
    list_display=[
        'id',
        'company_name',
        'plan_id',
    ]

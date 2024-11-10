from django.contrib import admin
from . import models


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at',)
    search_fields = ('name',)


admin.site.register(models.Brand, BrandAdmin)

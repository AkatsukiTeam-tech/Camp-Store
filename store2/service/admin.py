from django.contrib import admin
from .models import Category, Model

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {'slug' : ('name', )}
    save_on_top = True


class ModelAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "category", "sort", "active")
    list_display_links = ["name", "slug", "category", "sort", "active"]
    prepopulated_fields = {'slug' : ('name', )}
    list_filter = ["category", "active"]
    save_on_top = True


admin.site.register(Category, CategoryAdmin)
admin.site.register(Model, ModelAdmin)


from django.contrib import admin

# Register your models here.

from .models import ingredient, recipe,Comment
class Admin(admin.ModelAdmin):
    filter_horizontal = ("ingredientInmenu",)

admin.site.register(recipe,Admin)
admin.site.register(ingredient)
admin.site.register(Comment)


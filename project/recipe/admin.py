from django.contrib import admin

# Register your models here.

from .models import ingredient, recipe,Comment,Addrecipe
class Admin(admin.ModelAdmin):
    filter_horizontal = ("ingredientInmenu",)

admin.site.register(recipe,Admin)
admin.site.register(ingredient)
admin.site.register(Comment)
admin.site.register(Addrecipe)

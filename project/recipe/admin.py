from django.contrib import admin

# Register your models here.

from .models import ingredient, recipe,Comment,Addrecipe,order,search,petition
class Admin(admin.ModelAdmin):
    filter_horizontal = ("ingredientInmenu","member",'like',)

admin.site.register(recipe,Admin)
admin.site.register(ingredient)
admin.site.register(Comment)
admin.site.register(Addrecipe)
admin.site.register(order)
admin.site.register(search)
admin.site.register(petition)

from django.db import models

# Create your models here.

class ingredient(models.Model):
    class material(models.TextChoices):
        meat = "meat"
        carbohydrate = "carbohydrate"
        vegetable = "vegetable"
        condiment = "condiment"
        fruit = "fruit"
        other = "other"
    ingredient = models.CharField(max_length=100,default=None)
    type = models.CharField(max_length=100,
        choices=material.choices,
        default=material.other,
        )
    caloriePerUnit = models.IntegerField(default=None, null=True)

    def __str__(self) -> str:
        return f"{self.ingredient}"

class recipe(models.Model):

    class mode(models.TextChoices):
        normal = "normal"
        meat = "meat"
        vegan = "vegan"
        halal = "halal"
        beverag = "beverag"
        ovo = "oco vegen"
        vegy = "vegetarian"
        appetizer = "appetizer"

    class level(models.TextChoices):
        free = "free"
        price = "pay only"

    menu = models.CharField(max_length=100,default=None)
    ingredientInmenu =models.ManyToManyField(ingredient,blank=True,related_name="ingredientInrecipe")

    type = models.CharField(max_length=100,
        choices=mode.choices,
        default=mode.normal,
        )
    
    status = models.CharField(max_length=100,
        choices=level.choices,
        default=level.free,
        )
    


    def __str__(self) -> str:
        return f"{self.type}"


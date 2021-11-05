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

    def __str__(self) -> str:
        return f"{self.ingredient}"

class recipe(models.Model):

    class mode(models.TextChoices):
        dessert = "dessert"
        meat = "meat"
        halal = "halal"
        beverag = "beverag"
        ocovegen = "ocovegen"
        vegy = "vegetarian"
        appetizer = "appetizer"

    class level(models.TextChoices):
        free = "free"
        price = "pay only"

    pic = models.ImageField(upload_to="",blank=True,null=True)
    menu = models.CharField(max_length=100,default=None)
    ingredient_unit = models.TextField(blank=True)
    HowToDo = models.TextField(blank=True)
    ingredientInmenu =models.ManyToManyField(ingredient,blank=True,related_name="ingredientInrecipe")
    type = models.CharField(max_length=100,
        choices=mode.choices,
        default=None,
        )
    
    status = ''
    
    price = models.IntegerField(default=None, null=True)
    calorie = models.IntegerField(default=None, null=True)
    
    def __str__(self) -> str:
        return f"{self.menu}"


from django.db import models
from django.contrib.auth.models import User
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
    
    price = models.FloatField(default=None, null=True)
    calorie = models.IntegerField(default=None, null=True)
    member = models.ManyToManyField(User,blank=True,related_name="member")
    like = models.ManyToManyField(User,blank=True,related_name="like")


    def __str__(self) -> str:
        return f"{self.menu}"

class Comment(models.Model):
    post = models.ForeignKey(recipe,on_delete=models.CASCADE,related_name="comments")
    user=models.ForeignKey(User,default=None, on_delete=models.PROTECT)
    body = models.TextField(default=None)
    date_added =models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.post}"

class Addrecipe(models.Model):
    user=models.ForeignKey(User,default=None, on_delete=models.PROTECT)
    bankaccount = models.CharField(default=None,max_length=20)

    class status(models.TextChoices):
        no = "no"
        confirm = "confirm"

    class mode(models.TextChoices):
        dessert = "dessert"
        meat = "meat"
        halal = "halal"
        beverag = "beverag"
        ocovegen = "ocovegen"
        vegy = "vegetarian"
        appetizer = "appetizer"

    pic = models.ImageField(upload_to="",blank=True,null=True)
    menu = models.CharField(max_length=100,default=None)
    ingredient_unit = models.TextField(blank=True)
    HowToDo = models.TextField(blank=True)
    

    type = models.CharField(max_length=100,
        choices=mode.choices,
        default=None,
        )

    confirm = models.CharField(max_length=10,
        choices=status.choices,
        default=status.no,
        )

    price = models.IntegerField(default=None, null=True)
    calorie = models.IntegerField(default=None, null=True)
    
    def __str__(self) -> str:
        return f"{self.menu}"

class order (models.Model):
    class status(models.TextChoices):
        no = "no"
        confirm = "confirm"
    
    user=models.ForeignKey(User,default=None, on_delete=models.PROTECT,related_name="userbuy")
    order = models.ForeignKey(recipe,on_delete=models.CASCADE,default=None,related_name="menu_order")
    price = models.FloatField(default=None, null=True)
    pic = models.ImageField(upload_to="",blank=True,null=True)
    date = models.DateField(editable=True)
    time = models.TimeField(editable=True,default=None)
    name = models.CharField(max_length=100,default=None)
    bankaccount = models.CharField(default=None,max_length=4)
    confirm = models.CharField(max_length=10,
        choices=status.choices,
        default=status.no,
        )
    def __str__(self) -> str:
        return f"{self.name,self.time}"

class search (models.Model):
    user=models.ForeignKey(User,default=None, on_delete=models.PROTECT,related_name="usersearch")
    Have = models.ManyToManyField(ingredient,blank=True,related_name="Have")
    DontNeed =models.ManyToManyField(ingredient,blank=True,related_name="dontNeed")

    def __str__(self) -> str:
        return f"{self.user}"

class petition (models.Model):
    user=models.ForeignKey(User,default=None, on_delete=models.PROTECT)
    petition = models.TextField(blank=True)
    date_added =models.DateTimeField(auto_now_add=True)
    class status(models.TextChoices):
        no = "no"
        confirm = "confirm"
    confirm = models.CharField(max_length=10,
        choices=status.choices,
        default=status.no,
        )
    def __str__(self) -> str:
        return f"{self.user,self.date_added}"
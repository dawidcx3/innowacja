from django.db import models

# Create your models here.
    
class Color(models.Model):
    color_name = models.CharField(max_length=15)
   
class Cat(models.Model):
    cat_name = models.CharField(max_length=20)
    color_id = models.ForeignKey(Color, default=1, related_name="Color", on_delete=models.SET_DEFAULT)
    gender = models.BooleanField()
    
class Prey(models.Model):
    type = models.CharField(max_length=20)
    
class Hunting(models.Model):
    cat_id = models.ForeignKey(Cat, default=1, related_name="Cat", on_delete=models.SET_DEFAULT)
    prey_id = models.ForeignKey(Prey, default=1, related_name="Prey", on_delete=models.SET_DEFAULT)
    duration = models.DurationField()
      
class User(models.Model):
    user_name = models.CharField(max_length=20)
    cat1_id = models.ForeignKey(Cat, default=1, related_name="Cat1", on_delete=models.SET_DEFAULT)
    cat2_id = models.ForeignKey(Cat, default=1, related_name="Cat2", on_delete=models.SET_DEFAULT)
    cat3_id = models.ForeignKey(Cat, default=1, related_name="Cat3", on_delete=models.SET_DEFAULT)
    cat4_id = models.ForeignKey(Cat, default=1, related_name="Cat4", on_delete=models.SET_DEFAULT)
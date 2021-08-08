from django.db import models
from django.db.models.aggregates import Max
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

class Plants(models.Model):
    name = models.CharField(max_length=50, primary_key= True)
    latin_name = models.CharField(max_length=100, unique= True)
    isNative =  models.BooleanField(default= True)
    image_name = models.CharField(max_length=50)

    def __str__(self):
       return self.name

class Flowers(models.Model):
    plant = models.OneToOneField(Plants, on_delete= models.CASCADE)
    colors = models.TextField()
    desc = models.TextField()
    image_name = models.CharField(max_length=50, default= 'None.jpg')
    
    def __str__(self):
       return self.image_name

class Berries(models.Model):
    plant = models.OneToOneField(Plants, on_delete= models.CASCADE)
    image_name = models.CharField(max_length=50, default= 'None.jpg')
    colors = models.TextField()
    desc = models.TextField()
    

    def __str__(self):
       return self.image_name

class Leaves(models.Model):
    plant = models.OneToOneField(Plants, on_delete=models.CASCADE)
    image_name = models.CharField(max_length=50,  default= 'None.jpg')
    ARROW = 'AR'
    COMPOUND = 'CP'
    DELTOID = 'DL'
    HEART = 'HT'
    LANECOLATE = 'LA'
    LINEAR = 'LI'
    LOBED = 'LB'
    OBLONG = 'OB'
    OVAL = 'OL'
    THREE = 'TL'
    LEAF_SHAPE_CHOICES = [
        (ARROW, 'Arrow-Shaped'),
        (COMPOUND, 'Compound'),
        (DELTOID, 'Deltoid'),
        (HEART, 'Heart-Shaped'),
        (LANECOLATE, 'Lanecolate'),
        (LINEAR, 'Linear'),
        (LOBED, 'Lobed'),
        (OBLONG, 'Oblong'),
        (OVAL, 'Oval'),
        (THREE, 'Three-leaved')
    ]
    shapes = models.TextField()
    desc = models.TextField()


    def __str__(self):
       return self.image_name, self.shapes

class Stems(models.Model):
    plant = models.OneToOneField(Plants, on_delete=models.CASCADE)
    desc = models.TextField()


    def __str__(self):
       return self.plant

from django.db import models
from datetime import datetime # add to know the current time

# Create your table here.

class Product(models.Model):

    x = [
        ('phone','phone'),
        ('computer','coputer'),
        ('tele','tele'),
    ]
    # id ajouter auto
    name = models.CharField(max_length=50,default='zaid')# par defaut zaid 
    content = models.TextField(null =True) # n est pas obligatoir 
    price = models.DecimalField(max_digits=5,decimal_places=2)
    image = models.ImageField(upload_to='photos/%y/%m/%d',verbose_name='photo')# changer le nom d atribue
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=50,null=True,blank=True,choices=x)#choice list
    
    def __str__(self): # pour afficher les nom des objects en DB
        return self.name
    
    class Meta:
        verbose_name = 'phone' # pour afficher les nom du registre en DB
        ordering = ['name'] # trier par ordre


class Teste(models.Model):
    date = models.DateField() # type date
    time = models.TimeField(null=True) # type time
    created = models.DateTimeField(default=datetime.now) # date and time


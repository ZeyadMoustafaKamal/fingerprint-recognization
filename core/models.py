from django.db import models


class Finger(models.Model):

    choices = [
     
      ('id','id'),
      ('name','name')
    ]

    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='photos/%y/%m/%d',blank=True,null=True)
    age = models.CharField(max_length=100,default='age')
    phone = models.CharField(max_length=100,default='phone')
    adress = models.CharField(max_length=100,default='adress')
    datetime = models.DateTimeField(auto_now_add=True)
    activ = models.BooleanField(default=True)
    category = models.CharField(max_length=100, blank=True, null=True, choices=choices)

    def __str__(self):
        return self.name
    class Meta:
        ordering=['id']
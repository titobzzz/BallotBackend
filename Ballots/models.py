from django.db import models

from accounts.models import User



# Create your models here.

class Topics(models.Model):
    '''
    Represents trends and tags
    '''

    id = models.UUIDField(primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f"This is the {self.name} trend or tag"



class Ballots(models.Model):
    '''
    class for each ballot Posts 
    '''
    id = models.UUIDField(primary_key=True, unique=True, editable=False)
    tag = models.ForeignKey(Topics, default=None, on_delete=models.SET_NULL, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    images= models.ImageField(upload_to="Ballots/ballot_pictures",blank=True, null=True)
    # reactions= models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True) 
    


class Comment(models.Model):
    ''

    id = models.UUIDField(primary_key=True, unique=True, editable=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    ballot = models.ForeignKey(Ballots,on_delete=models.CASCADE)
    # reactions=
    #time
    content = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True) 
    tag = models.ForeignKey(Topics, default=None, on_delete=models.SET_NULL, null=True)
    

    

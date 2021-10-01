from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# The models will write the SQL for us. Djangos built-in ORM
# Users, tiles, 

#Setting up tile class for db storage
class Tile(models.Model):
    task = models.CharField(max_length=100)
    
    details = models.CharField(max_length=100)

    #textfield = unrerestricted text
    content = models.TextField()
    
    #Date -> grabs timezone
    date_posted = models.DateTimeField(default = timezone.now)

    #If a user is deleted, delete their tiles. 
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #Special method (dunder)
    def __str__(self):
        return self.task
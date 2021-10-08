from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



#Setting up Tile model
class Tile(models.Model):

    #Title of the task
    task = models.CharField(max_length=100)

    #A small description of the task
    details = models.CharField(max_length=100)

    #Content -> main body of content for task textfield = unrerestricted text
    content = models.TextField()
    
    #Date -> grabs timezone
    date_posted = models.DateTimeField(default = timezone.now)

    #If a user is deleted, delete their tiles. 
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #Special method (dunder)
    def __str__(self):
        return self.task



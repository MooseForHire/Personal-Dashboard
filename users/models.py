from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


#Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #Pillow libray isntalled
    image = models.ImageField(default='default.jpg', upload_to = 'profile pics')

    #User Profile
    def __str__(self):
        return f'{self.user.username} Profile'

    '''Save method - Resizing image to make it smaller!
    def save(self,*args,**kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)  
            img.thumbnail(output_size)
            img.save(self.image.path)'''
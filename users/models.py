from email.policy import default
from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    STATUS = (
        ('student','student'),
        ('proffisor','proffisor'),
        ('employee','employee')
    )
    LEVEL = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
    )
    COLLAGE = (
        ('هندسة معلوماتية','هندسة معلوماتية'),
        ('هندسة إتصالات','هندسة إتصالات'),
        ('طب بشري','طب بشري'),
        ('طب أسنان','طب أسنان'),
        ('هندسة معمارية','هندسة معمارية'),
        ('هندسة كهرباء','هندسة كهرباء'),
        ('هندسة طبية','هندسة طبية'),
        ('هندسة حاسبات','هندسة حاسبات'),
    )
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100,choices=STATUS,default='student')
    level = models.IntegerField(choices=LEVEL,blank=True,null=True)
    collage = models.CharField(max_length=100,choices=COLLAGE,default='هندسة معلوماتية')
    image = models.ImageField(upload_to='images/',blank=True,null=True,default='images/default/user.png')

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = 'images/default/user.png'
        return url

    def __str__(self):
        return self.username
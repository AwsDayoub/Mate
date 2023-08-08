from email.policy import default
from secrets import choice
from statistics import mode
from django.db import models
from django.template.defaultfilters import slugify
from users.models import CustomUser
import os

# Create your models here.

class Subject(models.Model):

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

    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('Subject', slugify(self.slug), instance)
        return None


    name = models.CharField(max_length=50)
    level = models.IntegerField(choices=LEVEL,null=True)
    collage = models.CharField(max_length=100,choices=COLLAGE,null=True)
    prof = models.CharField(max_length=100)
    image = models.ImageField(null=True,blank=True,upload_to='images/',default='images/default/group.png')

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = 'images/default/group.png'
        return url


    def __str__(self):
        return self.name


class Message(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    content = models.TextField()
    sender = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    send_date = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)

    def __str__(self):
        return self.content[:50]
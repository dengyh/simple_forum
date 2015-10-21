from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    nickname = models.CharField(max_length=64, blank=True, null=True)
    qq = models.CharField(max_length=16, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    email = models.CharField(max_length=16, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatar', blank=True, null=True)
    remark = models.CharField(max_length=256, blank=True, null=True)

    def __unicode__(self):
        return self.user.username + '\'s information'

    class Mata:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

def createUserProfile(sender, instance, created, **kwargs):
    if created:
        userProfile = UserProfile()
        userProfile.user = instance
        userProfile.save()

def deleteUserProfile(sender, instance, **kwargs):
    userProfile = UserProfile.objects.get(user=instance)
    userProfile.delete()

post_save.connect(createUserProfile, sender=User)
pre_delete.connect(deleteUserProfile, sender=User)
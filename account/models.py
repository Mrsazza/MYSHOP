from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length = 11, blank = True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length =100,blank=True)
    
    def __str__(self):
        return 'Profile For user {}'.format(self.user.username)

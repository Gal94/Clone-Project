from django.db import models
from django.contrib.auth.models import User
# Create your models here.


#my users model inherits on a one to one ratio from django's base user
class Users(models.Model):
    user = models.OneToOneField(User, on_delete='CASCADE') #data base of user tables

    def __str__(self):
        return "@{}".format(self.user.username)

from django.db import models


# Create your models here.


class Ending(models.Model):
    base_info = models.TextField()
    property_info = models.TextField()
    around_info = models.TextField()
    family_info = models.TextField()
    friends_info = models.TextField()
    pets_info = models.TextField()
    medical_info = models.TextField()
    inherit_info = models.TextField()
    contact_info = models.TextField()
    message_info = models.TextField()
    email = models.OneToOneField('users.User', on_delete=models.CASCADE)

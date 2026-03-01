from django.db import models
from django.contrib.auth.models import User


# Contact Model (keep this)
class Contact(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Profile Model (ADD THIS)
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    image = models.ImageField(
        upload_to='profile_pics/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username
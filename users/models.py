# users/models.py

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """
        Create and return a regular user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)  # Hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """
        Create and return a superuser with the given username, email, and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)
    
class User(AbstractUser):
    """
    User model that extends Django's AbstractUser.
    Includes additional fields for user roles and profile information.
    """
    is_teacher = models.BooleanField(
        default=False,
        help_text="Indicates if the user is a teacher. If False, the user is a student."
    )
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        null=True,
        help_text="User's profile picture. Optional field."
    )
    bio = models.TextField(
        max_length=500,
        blank=True,
        help_text="Short bio of the user. Maximum 500 characters."
    )

    def __str__(self):
        """
        String representation of the User model.
        Returns the username of the user.
        """
        return self.username
    
    # Use the default UserManager
    objects = UserManager()
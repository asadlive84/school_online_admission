from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

PANEL_TYPES = (
    ('1', 'Admin'),
    ('2', 'Manager'),
    ('3', 'Teacher'),
    ('4', 'Student'),
    ('5', 'Guest'),
)


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    """
        Custom User Model
    """

    full_name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    ac_status = models.BooleanField(default=False)
    user_type = models.CharField(max_length=1, choices=PANEL_TYPES, default='4')
    mobile_number = models.PositiveIntegerField(unique=True)
    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = ['full_name', 'username']

    objects = CustomUserManager()

    def __str__(self):
        return "{}-{}".format(self.full_name, self.username)

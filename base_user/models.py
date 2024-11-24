#---------- External Imports
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.timezone import now
import uuid
#---------- Internal Imports
from helper import keys

# --------------- User Manager 
class UserManager(BaseUserManager):
    """Custom user model manager."""

    def _create_user(self, email, password=None, is_superuser=False, is_staff=False, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        current = now()
        user = self.model(
            email=self.normalize_email(email),
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=current,
            date_joined=current,
            **extra_fields
        )
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, is_superuser=False, is_staff=False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, is_superuser=True, is_staff=True, **extra_fields)

# --------------- User Data Model
class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, editable=False, default = uuid.uuid4)
    email = models.EmailField(unique=True, error_messages={"unique": "A user with this email already exists."}, )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin_user = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """Check if the user has a specific permission."""
        return self.is_superuser

    def has_module_perms(self, app_label):
        """Check if the user has permissions for a specific app."""
        return self.is_superuser

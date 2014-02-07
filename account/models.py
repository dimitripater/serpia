from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class AccountUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=20, unique=True)
    about_me = models.TextField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = AccountUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
            return True

    @property
    def is_staff(self):
        return self.is_admin

    def __unicode__(self):
        return self.username
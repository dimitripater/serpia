from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify


class AccountUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    about_me = models.TextField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    slug = models.SlugField()
    has_profile = models.BooleanField(default=False)

    objects = AccountUserManager()

    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
            return True

    @property
    def is_staff(self):
        return self.is_admin

    def get_absolute_url(self):
        return reverse('accounts_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.email)

        super(Account, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.email
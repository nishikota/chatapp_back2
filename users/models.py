from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, username, password, company_name, **extra_fields):

        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, company_name=company_name, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, company_name, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, company_name, username, **extra_fields)

    def create_superuser(self, username, email, password, company_name, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, username, password, company_name, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(_('名前'), max_length=300, blank=False)
    email = models.EmailField(_('メールアドレス'), blank=False, unique=True)
    company_name = models.CharField('会社名', max_length=100,
    blank=False)
    section_name = models.CharField('部署名', max_length=100, blank=True)
    post_name = models.CharField('役職', max_length=100, blank=True)
    # room_id = models.ManyToManyField(Room)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'company_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

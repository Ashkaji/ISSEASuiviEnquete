import re

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import Group, AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, login, password=None, **extra_fields):
        if not login:
            raise ValueError("You must define a username")
        user = self.model(
            login=login,
            **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, login, password=None, **extra_fields):
        user = self.create_user(
            login=login,
            password=password,
            **extra_fields
        )
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user

    def set_password(self, raw_password):
        password_regex = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^\w\s]*)[A-Za-z\d]{10,}$'

        if not re.match(password_regex, raw_password):
            raise ValidationError(
                'Password must be at least 10 characters long and include at least one digit, '
                'one lowercase letter, and one uppercase letter. Special characters are optional but allowed.'
            )
        super().set_password(raw_password)


class CustomUser(AbstractBaseUser):
    login = models.CharField(max_length=16, unique=True, default='', validators=[RegexValidator(
        regex=r'^[A-Za-z0-9_]{3,15}$',
        message='Login name can only contain letters, digits, and underscores (3-15 characters).',
        code='invalid_login'
    )])
    role = models.CharField(max_length=15, null=False, blank=False, default='', choices=[
        ('interviewer', 'Interviewer'),
        ('supervisor', 'Supervisor'),
        ('headquarters', 'Headquarters'),
        ('observers', 'Observers'),
    ])
    supervisor = models.CharField(max_length=16, blank=True, null=True, default='', validators=[RegexValidator(
        regex=r'^[A-Za-z0-9_]{3,15}$',
        message='Login name can only contain letters, digits, and underscores (3-15 characters).',
        code='invalid_login'
    )])
    fullname = models.CharField(max_length=50, blank=False, null=False, default='')

    groups = models.ManyToManyField(Group, blank=True)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    class Meta:
        verbose_name = 'User'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the user object first
        if self.role:
            if self.role != 'headquarters':
                group_name = f"{self.role.capitalize()}s"
            else:
                group_name = f"{self.role.capitalize()}"
        else:
            group_name = "Observers"
        group, created = Group.objects.get_or_create(name=group_name)
        self.groups.add(group)

    def __str__(self):
        return f"{self.login}"


class StudentUser(CustomUser):
    idnumber = models.CharField(max_length=10, unique=True, default='', blank=True, null=True)
    gender = models.CharField(max_length=1, default='', choices=[('F', 'Female'), ('M', 'Male')])
    grade = models.CharField(max_length=11, null=False, blank=False, default='')
    nationality = models.CharField(max_length=3, default='', choices=[
        ('BFA', 'Burkina Faso'),
        ('BEN', 'Bénin'),
        ('CMR', 'Cameroun'),
        ('COG', 'Congo'),
        ('COD', 'RDC'),
        ('GAB', 'Gabon'),
        ('GNQ', 'Guinée-Equatoriale'),
        ('MDG', 'Madagascar'),
        ('NER', 'Niger'),
        ('CAF', 'République Centrafricaine'),
        ('TCD', 'Tchad'),
        ('TGO', 'Togo'),
    ])

    def __str__(self):
        return f"{self.login}: {self.fullname}"

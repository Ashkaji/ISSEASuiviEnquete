from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, Group
from django.db import models


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


class CustomUser(AbstractUser):
    login = models.CharField(max_length=10, unique=True, default='')
    # supervisor = models.CharField(max_length=10, null=True, blank=True, default='')
    fullname = models.CharField(max_length=50, blank=False, null=False, default='')
    phonenumber = models.CharField(max_length=10, default='')
    head_of_team = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, default='')

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    class Meta:
        verbose_name = 'User'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return f"{self.last_name.lower()}-{self.first_name.lower()}"


class Student(CustomUser):
    register = models.CharField(max_length=6, unique=True, default='', blank=True, null=True)
    gender = models.CharField(
        choices=[('F', 'Female'), ('M', 'Male')],
        max_length=1,
        default=''
    )
    grade = models.CharField(
        choices=[
            ('AS1', 'AS 1st Year'),
            ('AS2', 'AS 2nd Year'),
            ('ISEL1', 'ISE Long 1st Year'),
            ('ISEL2', 'ISE Long 2nd Year'),
            ('ISEL3', 'ISE Long 3rd Year'),
            ('ISE1-ECO', 'ISE1 Economics'),
            ('ISE1-MATHS', 'ISE1 Mathematics'),
            ('ISE2', 'ISE 2nd Year'),
        ],
        max_length=11,
        null=False,
        blank=False,
        default='',
    )

    nationality = models.CharField(max_length=10, default='')

    class Meta:
        abstract = True


class Interviewer(Student):
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        group_interviewers = Group.objects.get(name='Interviewers')
        self.groups.add(group_interviewers)


class Supervisor(Student):
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        group_supervisors = Group.objects.get(name='Supervisors')
        self.groups.add(group_supervisors)


class Headquarters:
    pass

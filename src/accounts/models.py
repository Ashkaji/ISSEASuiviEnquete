from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser, Group
from django.db import models


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, password=None, **extra_fields):
        if not username:
            raise ValueError("You must define a username")
        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, first_name='', last_name='', password=None, **extra_fields):
        user = self.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            **extra_fields
        )
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user


class CustomUser(AbstractUser):
    username = models.CharField(max_length=10, unique=True, default='')
    first_name = models.CharField(max_length=50, blank=False, null=False, default='')
    last_name = models.CharField(max_length=45, blank=False, null=False, default='')
    superieur = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, default='')

    USERNAME_FIELD = 'username'
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


class Supervisor(CustomUser):
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        group_controllers = Group.objects.get(name='Supervisors')
        self.groups.add(group_controllers)


class Student(CustomUser):
    number = models.CharField(max_length=6, unique=True, null=False, blank=False, default='')
    grade = models.CharField(
        choices=[
            ('AS1', 'AS 1st Year'),
            ('AS2', 'AS 2nd Year'),
            ('ISEL1', 'ISE Long 1st Year'),
            ('ISEL2', 'ISE Long 2nd Year'),
            ('ISEL3', 'ISE Long 3rd Year'),
            ('ISE1-ECO', 'ISE1 Economics'),
            ('ISE1-MATHS', 'ISE1-MATHS'),
            ('ISE2', 'ISE 2nd Year'),
        ],
        max_length=15,
        null=False,
        blank=False,
        default=''
    )
    gender = models.CharField(
        choices=[('F', 'Female'), ('M', 'Male')],
        max_length=1,
        default=''
    )
    nationality = models.CharField(max_length=10, default='')

    class Meta:
        abstract = True


class Interviewer(Student):
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        group_interviewers = Group.objects.get(name='Interviewers')
        self.groups.add(group_interviewers)


class Controller(Student):
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        group_controllers = Group.objects.get(name='Controllers')
        self.groups.add(group_controllers)


class SubSupervisor(Student):
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        group_controllers = Group.objects.get(name='SubSupervisors')
        self.groups.add(group_controllers)

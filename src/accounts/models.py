from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser
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


class Superviseur(CustomUser):
    pass


class Etudiant(CustomUser):
    matricule = models.CharField(max_length=6, unique=True, null=False, blank=False, default='')
    classe = models.CharField(
        choices=[
            ('AS1', 'AS 1ere annee'),
            ('AS2', 'AS 2e annee'),
            ('ISEL1', 'ISE Long 1ere annee'),
            ('ISEL2', 'ISE Long 2e annee'),
            ('ISEL3', 'ISE Long 3e annee'),
            ('ISE1-ECO', 'ISE1 Economie'),
            ('ISE1-MATHS', 'ISE1-MATHS'),
            ('ISE2', 'ISE 2e annee'),
        ],
        max_length=15,
        null=False,
        blank=False,
        default=''
    )
    sexe = models.CharField(
        choices=[('F', 'Feminin'), ('M', 'Masculin')],
        max_length=1,
        default=''
    )
    nationnalite = models.CharField(max_length=10, default='')

    class Meta:
        abstract = True


class Enqueteur(Etudiant):
    pass


class Controleur(Etudiant):
    pass


class SupersiveurAssistant(Etudiant):
    pass

from django.contrib import admin

from accounts.models import CustomUser, Superviseur, Enqueteur, Controleur, SupersiveurAssistant


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'last_name',
        'first_name',
    )
    empty_value_display = 'unknown'


@admin.register(Superviseur)
class SuperviseurAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'last_name',
        'first_name',
    )
    list_per_page = 50
    empty_value_display = 'unknown'


@admin.register(Enqueteur)
class EnqueteurAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'matricule',
        'last_name',
        'first_name',
        'classe',
        'sexe',
        'nationnalite',
    )
    list_per_page = 50
    empty_value_display = 'unknown'


@admin.register(Controleur)
class ControleurAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'matricule',
        'last_name',
        'first_name',
        'classe',
        'sexe',
        'nationnalite',
    )
    list_per_page = 50
    empty_value_display = 'unknown'


@admin.register(SupersiveurAssistant)
class SupersiveurAssistantAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'matricule',
        'last_name',
        'first_name',
        'classe',
        'sexe',
        'nationnalite',
    )
    list_per_page = 50
    empty_value_display = 'unknown'

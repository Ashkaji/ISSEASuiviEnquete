from django.contrib import admin

from accounts.models import CustomUser, Supervisor, SubSupervisor, Controller, Interviewer


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'last_name',
        'first_name',
    )
    empty_value_display = 'unknown'


@admin.register(Supervisor)
class SupervisorAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'last_name',
        'first_name',
    )
    list_per_page = 50
    empty_value_display = 'unknown'


@admin.register(SubSupervisor)
class SubSupervisorAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'number',
        'last_name',
        'first_name',
        'grade',
        'gender',
        'nationality',
    )
    list_per_page = 50
    empty_value_display = 'unknown'


@admin.register(Controller)
class ControllerAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'number',
        'last_name',
        'first_name',
        'grade',
        'gender',
        'nationality',
    )
    list_per_page = 50
    empty_value_display = 'unknown'


@admin.register(Interviewer)
class InterviewerAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'number',
        'last_name',
        'first_name',
        'grade',
        'gender',
        'nationality',
    )
    list_per_page = 50
    empty_value_display = 'unknown'

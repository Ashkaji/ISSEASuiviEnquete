from django.contrib import admin

from accounts.models import CustomUser, StudentUser


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'login',
        'role',
        'supervisor',
    )
    empty_value_display = 'unknown'


@admin.register(StudentUser)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'idnumber',
        'fullname',
        'gender',
        'grade',
        'nationality',
        'role',
        'login',
    )
    empty_value_display = 'unknown'

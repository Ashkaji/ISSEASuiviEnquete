from django.contrib import admin

from accounts.models import CustomUser, Supervisor, Interviewer


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'fullname',
        'email',
    )
    empty_value_display = 'unknown'


@admin.register(Interviewer)
class InterviewerAdmin(admin.ModelAdmin):
    list_display = (
        'fullname',
        'grade',
        'gender',
        'nationality',
        'phonenumber',
    )
    list_per_page = 50
    empty_value_display = 'unknown'

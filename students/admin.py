from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'full_name', 'phone_number', 'is_registered')
    list_filter = ('is_registered',)
    search_fields = ('full_name', 'registration_number', 'phone_number')
    list_per_page = 20

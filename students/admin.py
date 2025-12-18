from django.contrib import admin
from .models import Student
from django.urls import path, reverse
from django.shortcuts import redirect
from django.utils.html import format_html

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'full_name', 'phone_number', 'is_registered')
    list_filter = ('is_registered',)
    search_fields = ('full_name', 'registration_number', 'phone_number')
    list_per_page = 20

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            # Redirect to the main export view which is not under admin namespace
            path('export/', self.admin_site.admin_view(self.export_redirect), name='export_students_proxy'),
        ]
        return custom_urls + urls

    def export_redirect(self, request):
        return redirect(reverse('export_students'))

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['export_url'] = reverse('admin:export_students_proxy')
        return super().changelist_view(request, extra_context)

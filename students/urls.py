from django.urls import path, include
from .views import student_login, student_dashboard, student_update, add_student, export_students

urlpatterns = [
    path('', student_login, name='student_login'),
    path('dashboard/', student_dashboard, name='student_dashboard'),
    path('student/<int:pk>/update/', student_update, name='student_update'),
    path('add/', add_student, name='add_student'),
    path('export/', export_students, name='export_students'),
    # Ongeza URL za uthibitishaji za Django (kwa login/logout)
    path('accounts/', include('django.contrib.auth.urls')),
]
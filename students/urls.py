from django.urls import path, include
from .views import student_login, student_dashboard, student_update, add_student

urlpatterns = [
    path('', student_login, name='student_login'),
    path('dashboard/', student_dashboard, name='student_dashboard'),
    path('student/<int:pk>/update/', student_update, name='student_update'),
    path('add/', add_student, name='add_student'),
    # Ongeza URL za uthibitishaji za Django (kwa login/logout)
    path('accounts/', include('django.contrib.auth.urls')),
]
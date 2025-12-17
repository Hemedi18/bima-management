from django.db import models

class Student(models.Model):
    registration_number = models.CharField(max_length=50, unique=True, verbose_name="Registration Number")
    full_name = models.CharField(max_length=255, unique=True, verbose_name="Full Name")
    phone_number = models.CharField(max_length=15, null=True, verbose_name="Phone Number")
    is_registered = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
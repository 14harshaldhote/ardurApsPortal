from django.db import models
from django.contrib.auth.models import User, Group

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    blood_group = models.CharField(max_length=10, null=True, blank=True)
    hire_date = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
        null=True, blank=True
    )
    panno = models.CharField(max_length=20, default="UNKNOWN")
    job_description = models.CharField(max_length=100, default="Not Assigned")
    employment_status = models.CharField(max_length=50)
    emergency_contact_address = models.TextField(default="Unknown")
    emergency_contact_primary = models.CharField(max_length=15, default="0000000000")
    emergency_contact_name = models.CharField(max_length=100, default="Unknown")
    start_date = models.DateField(null=True, blank=True)
    work_location = models.CharField(max_length=100, null=True)
    contact_number_primary = models.CharField(max_length=15, null=True, blank=True, default="0000000000")
    personal_email = models.EmailField(default="not_provided@example.com")
    aadharno = models.CharField(max_length=12, null=True, blank=True, default="UNKNOWN")
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

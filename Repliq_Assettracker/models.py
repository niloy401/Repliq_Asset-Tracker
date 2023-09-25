from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=100)
    employees = models.ManyToManyField(User, through='CompanyEmployeeRelationship')

class CompanyEmployeeRelationship(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    delegated_devices = models.ManyToManyField('Device', through='DeviceAssignment')

class Device(models.Model):
    name = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    checkout_logs = models.ManyToManyField('DeviceLog', related_name='checkouts', blank=True)
    return_logs = models.ManyToManyField('DeviceLog', related_name='returns', blank=True)

class DeviceAssignment(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee_relation = models.ForeignKey(CompanyEmployeeRelationship, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    condition = models.CharField(max_length=100)

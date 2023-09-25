from django.contrib import admin
from .models import Company, Device, CompanyEmployeeRelationship, DeviceAssignment, DeviceLog

admin.site.register(Company)
admin.site.register(Device)
admin.site.register(CompanyEmployeeRelationship)
admin.site.register(DeviceAssignment)
admin.site.register(DeviceLog)


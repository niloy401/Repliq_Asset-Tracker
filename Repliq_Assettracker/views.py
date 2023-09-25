from rest_framework import viewsets
from .models import Company, Device, CompanyEmployeeRelationship, DeviceAssignment, DeviceLog
from .serializers import CompanySerializer, DeviceSerializer, CompanyEmployeeRelationshipSerializer, DeviceAssignmentSerializer, DeviceLogSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class CompanyEmployeeRelationshipViewSet(viewsets.ModelViewSet):
    queryset = CompanyEmployeeRelationship.objects.all()
    serializer_class = CompanyEmployeeRelationshipSerializer

class DeviceAssignmentViewSet(viewsets.ModelViewSet):
    queryset = DeviceAssignment.objects.all()
    serializer_class = DeviceAssignmentSerializer

class DeviceLogViewSet(viewsets.ModelViewSet):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer

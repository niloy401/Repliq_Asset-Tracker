from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, DeviceViewSet, CompanyEmployeeRelationshipViewSet, DeviceAssignmentViewSet, DeviceLogViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'employee-relationships', CompanyEmployeeRelationshipViewSet)
router.register(r'device-assignments', DeviceAssignmentViewSet)
router.register(r'device-logs', DeviceLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
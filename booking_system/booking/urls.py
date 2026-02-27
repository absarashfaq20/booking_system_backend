# booking/urls.py
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, ServiceProviderViewSet, TimeSlotViewSet, AppointmentViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'providers', ServiceProviderViewSet)
router.register(r'timeslots', TimeSlotViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = router.urls
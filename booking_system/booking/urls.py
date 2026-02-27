from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    ServiceViewSet,
    ServiceProviderViewSet,
    TimeSlotViewSet,
    AppointmentViewSet,
    UserSignupView
)

# -------------------------------
# 1️⃣ Router for viewsets
router = DefaultRouter()
router.register("services", ServiceViewSet)
router.register("providers", ServiceProviderViewSet)
router.register("timeslots", TimeSlotViewSet)
router.register("appointments", AppointmentViewSet)

# -------------------------------
# 2️⃣ URL patterns
urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
]

# 3️⃣ Include router URLs
urlpatterns += router.urls
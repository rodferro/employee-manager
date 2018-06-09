from django.conf.urls import url, include
from rest_framework import routers
from manager.api.views import EmployeeViewSet


router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet, base_name='employee')

urlpatterns = [
    url(r'^', include(router.urls)),
]
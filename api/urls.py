from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import EnterpriseCreateList, EmployeeCreateList

router = routers.DefaultRouter()
router.register('enterprise_create', EnterpriseCreateList.as_view())
router.register('employee_create', EmployeeCreateList.as_view())

urlpatterns = [
    path('',include(router.urls)),
]

# urlpatterns = router.urls


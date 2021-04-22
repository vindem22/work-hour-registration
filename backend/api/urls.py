from api.views import EmployeeDetailViewSet, EmployeeViewSet, RecordViewSet
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee', EmployeeViewSet)
router.register('employee_record',EmployeeDetailViewSet)
router.register('record',RecordViewSet)

urlpatterns = []
app_name = 'api'
urlpatterns +=router.urls


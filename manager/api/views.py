# from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    pagination_class = None
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all().order_by('name')
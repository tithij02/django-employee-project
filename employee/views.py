from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    try:
        employee = Employee.objects.get(email=email, password=password)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    except Employee.DoesNotExist:
        return Response({"error": "Invalid credentials"}, status=400)

@api_view(['POST'])
def register(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"success": True})
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def find_by_email(request):
    email = request.GET.get('email')
    try:
        employee = Employee.objects.get(email=email)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"}, status=404)

@api_view(['GET'])
def get_all(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_by_id(request):
    emp_id = request.GET.get('id')
    try:
        employee = Employee.objects.get(id=emp_id)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"}, status=404)

@api_view(['PUT'])
def update(request):
    try:
        emp_id = request.data.get('id')
        employee = Employee.objects.get(id=emp_id)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True})
        return Response(serializer.errors, status=400)
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"}, status=404)

@api_view(['DELETE'])
def delete(request):
    emp_id = request.GET.get('id')
    try:
        employee = Employee.objects.get(id=emp_id)
        employee.delete()
        return Response({"success": True})
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"}, status=404)



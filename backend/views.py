from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.db import IntegrityError
from django.db.models import Q, Sum, F
from django.http import JsonResponse, response, HttpResponse
from requests import get
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from ujson import loads as load_json
from django.http import HttpResponse

from backend.models import Employees
from backend.serializers import EmployeesSerializer


# Create your views here.

class IndexView(ListAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer

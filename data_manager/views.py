from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseRedirect, HttpResponseNotFound
import re, csv
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.urls import reverse
from django.conf import settings
from .models import DataFile, Industry, YearFounded, City, State, Company, Country
import pandas as pd
import csv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Company
from .serializers import FilterSerializer

def login_page(request):
    logout(request)
    return render(request, 'login.html')

def login_user_with_google(request):
    return render(request, 'upload_data.html', {"app_name": "upload_data"})

@login_required
def upload_data(request):
    return render(request, 'upload_data.html', {"app_name": "upload_data"})

@login_required
def query_builder(request):
    industries = Company.objects.values('industry').exclude(industry=None).order_by('industry').distinct()
    year_founded = Company.objects.values('year_founded').exclude(year_founded=None).order_by('year_founded').distinct()
    cities = Company.objects.values('city').exclude(city=None).order_by('city').distinct()
    states = Company.objects.values('state').exclude(state=None).order_by('state').distinct()
    countries = Company.objects.values('country').exclude(country=None).order_by('country').distinct()
    return render(request, 'query_builder.html', {"industries": industries, "year_founded": year_founded, "cities": cities, "states": states, "countries": countries})

@login_required
def users_list(request):
    users = User.objects.all().order_by('id')
    return render(request, 'users_list.html', {"app_name": "users_list", "users": users})

@login_required
def add_user(request):
    user = request.user
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    username = request.POST.get('username')
    password = request.POST.get('pass')
    cpassword = request.POST.get('cpass')
    error_message = ""
    emailRegex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    passwordRegex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    
    if fname == "":
        error_message = "First name cannot be empty"
    elif lname == "":
        error_message = "Last name cannot be empty"
    elif email == "":
        error_message = "Email cannot be empty"
    elif not bool(re.search(emailRegex, email)):
        error_message = "Email is no valid"
    elif username == "":
        error_message = "Username cannot be empty"
    elif password == "":
        error_message = "Passowrd cannot be empty"
    elif not bool(re.search(passwordRegex, password)):
        error_message = "Passowrd does not meet the criteria"
    elif cpassword == "":
        error_message = "Confirm Passowrd cannot be empty"
    elif not bool(re.search(passwordRegex, cpassword)):
        error_message = "Confirm Password does not meet the criteria"
    elif password != cpassword:
        error_message = "Password and confirm password cannot be different"
    
    if error_message != "":
        return HttpResponseBadRequest(error_message)
    user = User.objects.create_user(first_name=fname.capitalize(),last_name=lname.capitalize(),email=email,username=username,password=password)
    return JsonResponse({"new_user_data": {"id": user.id, "full_name": user.get_full_name(), "email": user.email, "status": user.is_active}})


@login_required
def delete_user(request):
    user = request.user
    user_id = request.POST.get('user_id')
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return HttpResponse()
    except Exception as e:
        return HttpResponseBadRequest("User not found")


def create_db(file_path):
    chunk_size = 100  # Number of rows per chunk
    for chunk in pd.read_csv(file_path, delimiter=',', chunksize=chunk_size, header=None):
        companies = []
        for index, row in chunk.iterrows():
            if index == 0: continue
            company = Company(
                name = row[1],
                domain = row[2],
                year_founded = int(float(row[3])) if pd.notna(row[3]) else None,
                industry = row[4] if pd.notna(row[4]) else None,
                size_range = row[5] if pd.notna(row[5]) else None,
                city = row[6].split(",")[0] if pd.notna(row[6]) else None,
                state = row[6].split(",")[1] if pd.notna(row[6]) else None,
                country = row[6].split(",")[2] if pd.notna(row[6]) else None,
                linkedin_url = row[8] if pd.notna(row[8]) else None,
                current_employee_estimate = row[9] if pd.notna(row[9]) else None,
                total_employee_estimate = row[10] if pd.notna(row[10]) else None
            )
            companies.append(company)
        Company.objects.bulk_create(companies)


def upload_file(request):
    if request.method == "POST":
        file = request.FILES.get('file')
        obj = DataFile.objects.create(file=file)
        create_db(obj.file)
    return JsonResponse({"data": "Data uploaded successfully"})


class FilterRecordsView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = FilterSerializer(data=request.data)
        if serializer.is_valid():
            filters = serializer.validated_data
            queryset = Company.objects.all()

            if filters.get('keyword'):
                queryset = queryset.filter(name__icontains=filters['keyword'])
            if filters.get('industry'):
                queryset = queryset.filter(industry=filters['industry'])
            if filters.get('city'):
                queryset = queryset.filter(city=filters['city'])
            if filters.get('state'):
                queryset = queryset.filter(state=filters['state'])
            if filters.get('country'):
                queryset = queryset.filter(country=filters['country'])
            if filters.get('year_founded'):
                queryset = queryset.filter(year_founded=filters['year_founded'])
            if filters.get('employees_from'):
                queryset = queryset.filter(employees=filters['employees_from'])
            if filters.get('employees_to'):
                queryset = queryset.filter(employees=filters['employees_to'])

            record_count = queryset.count()
            return Response({'record_count': record_count}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
def CreateAccount(request):
    if request.method == "POST":
        if request.content_type == 'application/json':
            status= 'Pass'
            status_memo=''
            #print(request.body)
            
            if request.body:
                # Decode data to a dict object
                json_data = json.loads(request.body)                            

            user_name = json_data["username"]
            password = json_data["password"]          
            #check user name already exist or not
            userList= User.objects.filter(user_name=user_name)
            if(len(userList)>0):
                status = False
                status_memo = 'Username already exists'
            
            # constraint with username and password
            if(len(user_name)<3 or len(user_name)>32):
                status = False
                status_memo = 'Account Length too short/too long'
            if(len(password)<8 or len(password)>32):
                status = False
                status_memo = 'Password Length too short/too long'
            if(password.islower() or password.isupper() or not any(char.isdigit() for char in password)):
                status = False
                status_memo = 'password need containing at least 1 uppercase letter, 1 lowercase letter, and 1 number.'                   
            
            encry_pass= make_password(password)

            if status :
                try:
                    obj= User(user_name=user_name,password=encry_pass)
                    obj.save()
                except Exception as e:
                    print(e)                
        else:
            status = False
            status_memo = 'content type is not JSON,please confirm the input data'
        return JsonResponse({"success":status ,"reason":status_memo})

    elif request.method == "GET" or request.method == "PUT" or request.method == "DELETE":
        return JsonResponse({"success":False ,"reason":"Wrong Method reuest"})
    else:
        return JsonResponse({"success":False ,"reason":"Other Question"})
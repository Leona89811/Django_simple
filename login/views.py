import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from users.models import User
from django.contrib.auth.hashers import check_password
import datetime

# Create your views here.
def VerifyAccount(request):
    if request.method == "POST":
        if request.content_type == 'application/json':
            if request.body:
                # Decode data to a dict object
                json_data = json.loads(request.body)    

            user_name = json_data["username"]
            password = json_data["password"]

            #list_display = [field.password for field in User._meta.fields]
            userList= User.objects.filter(user_name=user_name)
            if(len(userList)>0):
                #print(userList)
                #print(userList[0].password)
                #if(password==userList[0].password):
                if(check_password(password, userList[0].password)):
                    userList[0].error_count=-1
                    userList[0].save()
                    success= True
                    status_memo='Welcome login'
                else:
                    success= False
                    #update error count
                    if (userList[0].error_count < 4):
                        userList[0].error_count=userList[0].error_count+1
                        userList[0].save()
                        status_memo='Password is not match,please try again'
                    else:
                        #print(datetime.datetime.now())
                        #print(userList[0].update_time)
                        duration = datetime.datetime.now() - userList[0].update_time.replace(tzinfo=None)
                        #print(duration.total_seconds())
                        if(duration.total_seconds()<60):
                            status_memo='Login Fail over 5 times,Please wait for 1 minute'
                        else:
                            userList[0].save()
                            status_memo='Password is not match,please try again'
            else:
                success= False
                status_memo='user is not register ,please try again'

        else:
            success = False
            status_memo = 'content type is not JSON,please confirm the input data'
        
        return JsonResponse({"success":success ,"reason":status_memo})
    elif request.method == "GET" or request.method == "PUT" or request.method == "DELETE":
        return JsonResponse({"success":False ,"reason":"Wrong Method reuest"})
    else:
        return JsonResponse({"success":False ,"reason":"Other Question"})
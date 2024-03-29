import requests
import json

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from users.models import *
from general.models import *
from .serializers import *
from api.v1.general.functions import randomnumber
from django.utils import timezone



@api_view(['POST'])
@permission_classes((AllowAny,))
def signup_enter_details(request):
    serialized_data = RegisterSerializer(data=request.data)
    if serialized_data.is_valid():
        name = request.data['name']
        phone = request.data['phone']
        email = request.data['email']
        country = request.data['country']
        password = request.data['password']
        if Country.objects.filter(web_code=country).exists():
            country = Country.objects.get(web_code=country)
            if Profile.objects.filter(phone=phone, is_verified=False).exists():
                profile = Profile.objects.get(phone=phone, is_verified=False)
                if OtpRecord.objects.filter(phone=phone, is_applied=False).exists():
                    otp_record = OtpRecord.objects.filter(phone=phone, is_applied=False).latest("date_added")
                    if otp_record.attempts <=4:
                        otp = otp_record.otp
                        otp_record.attempts += 1
                        otp_record.date_updated = timezone.now()
                        otp_record.save()
                        #send this otp using fast2 sms
                        response_data = {
                            "StatusCode": 6000,
                            'data': {
                                "phone" : phone,
                                "title": "Success",
                                "message": "OTP send succesfully",
                            }
                        }
                    else:
                        response_data = {
                            'Statuscode' : 6001,
                            'data' : {
                                'title': 'failed',
                                'message' : "OTP limit exceeded"
                            }
                        }
                else:
                    otp = randomnumber(4)
                    otp_record = OtpRecord.objects.create(
                        phone = phone,
                        otp = otp,
                        country = country
                    )
                    profile.otp = otp
                    profile.save()
                    response_data = {
                        "StatusCode": 6000,
                        'data': {
                            "phone" : phone,
                            "title": "Success",
                            "message": "OTP send succesfully",
                        }
                    }

            elif Profile.objects.filter(phone=phone, is_verified=True).exists():
                response_data = {
                    'Statuscode' : 6001,
                    'data' : {
                        'title': 'failed',
                        'message' : "This number already verified"
                    }
                }
            else:
                otp = randomnumber(4)
                profile = Profile.objects.create(
                    name = name,
                    phone = phone,
                    email = email,  
                    password = password,
                    username = email ,
                    otp = otp,
                    auto_id = get_auto_id(Profile)            
                )

                if OtpRecord.objects.filter(phone=phone, is_applied=False).exists():
                    otp_instance = OtpRecord.objects.filter(phone=phone, is_applied=False).latest('date_added')
                    if otp_instance.attempts<=4:
                        otp_number = otp_record.otp
                        otp_instance.attempts += 1
                        otp_instance.date_updated = timezone.now()
                        otp_instance.save()
                        response_data = {
                            "StatusCode": 6000,
                            'data': {
                                "phone" : phone,
                                "title": "Success",
                                "message": "OTP send succesfully",
                            }
                        }
                    
                    else:
                        time_limit = otp_instance.date_updated + timezone.timedelta(days=1)
                        if time_limit <=timezone.now():
                            #Generate OTP
                                otp = randomnumber(4)

                                #Set OTP Record instance
                                otp_instance = OtpRecord.objects.create(
                                    country = country,
                                    phone = phone,
                                    otp = otp,                                  
                                )

                                #Set profile instance
                                profile.otp = otp_instance.otp
                                profile.save()
                                response_data = {
                                    "StatusCode": 6000,
                                    'data': {
                                        "phone" : phone,
                                        "title": "Success",
                                        "message": "OTP send succesfully",
                                    }
                                }
                        else:
                            response_data = {
                                "StatusCode": 6001,
                                'data':{
                                    "title": "Failed!",
                                    "message": "You crossed the maximum limit of OTPs."
                                }
                            }
                else:
                    otp_instance = OtpRecord.objects.create(
                        country = country,
                        phone = phone,
                        otp = otp,
                    )
                    profile.otp = otp_instance.otp
                    profile.save() 
                    response_data = {
                        "StatusCode": 6000,
                        'data': {
                            "phone" : phone,
                            "title": "Success",
                            "message": "OTP send succesfully",
                        }
                    }            
        else:
            response_data = {
                'Statuscode' : 6001,
                'data' : {
                    'title': 'failed',
                    'message' : "Service not available in this country"
                }
            }
    else:
        print("=====serialized._errors=======",serialized_data._errors)
        response_data = {
            "StatusCode": 6001,
            "data":{
                "title": "Validation Error",
                "message": serialized_data._errors
            }
        }

    return Response(response_data, status=status.HTTP_200_OK)
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


@api_view(['POST'])
@permission_classes((AllowAny,))
def signup_enter_details(request):
    serialized_data = RegisterSerializer(data=request.data)
    if serialized_data.is_valid():
        name = request.data['name']
        phone = request.data['phone']
        email = request.data['email']
        country = request.data['email']
        password = request.data['email']
        if Country.objects.filter(web_code=country).exists():
            if Profile.objects.filter(phone=phone, is_verified=False).exists():
                if OtpRecord.objects.filter(phone=phone, is_applied=False).exists():
                    otp_record = OtpRecord.objects.filter(phone=phone, is_applied=False).latest("date_added")
                    if otp_record.attempts <=4:
                        otp = otp_record.otp
                        #send this otp using fast2 sms
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
                    otp = otp             
                )
        else:
            response_data = {
                'Statuscode' : 6001,
                'data' : {
                    'title': 'failed',
                    'message' : "Service not available in this country"
                }
            }

    return Response(response_data, status=status.HTTP_200_OK)
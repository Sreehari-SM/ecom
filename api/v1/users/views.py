import requests
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from users.models import *
from general.models import *
from .serializers import *


@api_view(['POST'])
def signup_enter_details(request):
    serialized_data = RegisterSerializer(data=request.data)
    if serialized_data.is_valid():
        name = request.data['name']
        phone = request.data['phone']
        email = request.data['email']
        country = request.data['email']
        if Country.objects.filter(web_code=country).exists():
            pass
            # if Profile.objects.filter(phone=phone, is_verified=False).exists():
                # if OtpRecord.objects.filter(phone=phone, is_applied=False).exists():
        else:
            response_data = {
                'Statuscode' : 6001,
                'data' : {
                    'title': 'failed',
                    'message' : "Service not available in this country"
                }
            }

    return Response(response_data, status=status.HTTP_200_OK)
from api.models import Employee
import json
import requests
from django.conf import settings

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from rest_framework.views import APIView

from rest_framework_social_oauth2.views import TokenView
from authentication.models import CoreUser
from api.models import Employee
from authentication.serializers import (
    AuthUserModelSerializer,
    RegistrationDataValidationSerializer,
    RegistrationSerializer,

)



# Create your views here.

class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Employee.objects.all()
    serializer_class = AuthUserModelSerializer

    
    @action(methods=['get'], detail=False)
    def user(self, request):
        """
        User profile information
        """
        user = request.user
        if user:
            ser = self.serializer_class(user)
            return Response({'data': ser.data}, status=status.HTTP_200_OK)
            
        else:
            return Response(
                {
                    'status': status.HTTP_404_NOT_FOUND,
                    'error': 'User not found',
                }
            )

    
    @action(
        methods=['post'],
        detail=False,
        permission_classes=(AllowAny,),
        serializer_class=RegistrationDataValidationSerializer,
    )
    def register(self, request):
        """
        User registration
        """
        ser_params = self.serializer_class(data=request.data)
        ser_params.is_valid(raise_exception=True)
        data = ser_params.validated_data
        ser = RegistrationSerializer()
        ser.save(data=data)
        return Response(
        {'data': 'Success'}, status=status.HTTP_200_OK,
    )

    
class UserToken(TokenView):
    """
    Implements an endpoint to provide access tokens

    The endpoint is used in the following flows:

    * Authorization code
    * Password
    * Client credentials
    """

    def post(self, request, *args, **kwargs):

        request._request.POST = request._request.POST.copy()
        for key, value in request.data.items():
            request._request.POST[key] = value

        url, headers, body, status = self.create_token_response(
            request._request
        )

        body = json.loads(body)
        print(body)
        try:
            if body['error']:
                if body['error'] == 'invalid_grant':
                    if self.is_user_exist(request.data.get('username')):
                        body['error_description'] = 'Invalid password.'
                    else:
                        body['error_description'] = 'User not found'
                        status = 404
                if body['error'] == 'unsupported_grant_type':
                    body['error_decription'] = 'Invalid grant type.'
        except KeyError:
            pass
        response = Response(data=body, status=status)

        for k, v in headers.items():
            response[k] = v
        return response

    def is_user_exist(self, username=None):
        if username:
            return CoreUser.objects.filter(email=username).exists()
        
        return False

from rest_framework.permissions import BasePermission
from django.conf import settings
from rest_framework.exceptions import APIException
from rest_framework import status
import requests



class AuthenticationFailed(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = 'Given token not valid for any token type'
    default_code = 'authentication_failed'

class IsAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        token = request.headers.get('Authorization')
        if not token:
            return False
        token = token.split(' ')[1] # 'Bearer <token>'
        userAuthURL = f"{settings.USERSERVICE_URL}/get_user_info"
        headers = {"Authorization":f"Bearer {token}"}
        try:
            response = requests.get(userAuthURL, headers=headers)
            if response.status_code == 401:
                raise AuthenticationFailed()
            response.raise_for_status()
            user_data = response.json()
            # request.META['USER_DATA'] = user_data
            request.user = user_data
            return True
        except requests.exceptions.RequestException:
            return False


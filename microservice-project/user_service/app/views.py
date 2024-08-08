from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from app.uitlity import capture_error
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
User = get_user_model()
# Create your views here.


class DictToObject:
    def __init__(self, dict_obj):
        for key, value in dict_obj.items():
            setattr(self, key, value)

class signupJsonValidator:
    
    def request_validate(self,data:dict) -> object:
        if "email" not in data:
            raise ValueError("'email' parameter is missing")
        if "password" not in data:
            raise ValueError("'password' parameter is missing")
        return DictToObject(data)
    

class UserService:
    def create(self,data:object) -> object:
        user = User.objects.create(email=data.email)
        user.password = make_password(data.password)
        user.save()
        return user


@api_view(['POST'])
@capture_error
def signup(requset):
    jsonvalidator = signupJsonValidator()
    request_data = jsonvalidator.request_validate(requset.data)
    userService = UserService()
    userService.create(request_data)
    response = {"message":'signup is success'}
    return JsonResponse(response,status=201)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
@capture_error
def get_user_info(request):
    user_row = {
        "id":request.user.id,
        "email":request.user.email
    }
    return JsonResponse(user_row,status=200)

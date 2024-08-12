from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import AbstractBaseUser, update_last_login
from typing import Any, Dict, Optional, Type, TypeVar
from rest_framework_simplejwt.tokens import RefreshToken, SlidingToken, Token, UntypedToken



class TokenObtainPairSerializer(TokenObtainSerializer):
    token_class = RefreshToken

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        # data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)
        return data
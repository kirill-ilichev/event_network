import traceback
from django.utils.functional import SimpleLazyObject
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth.middleware import get_user
from django.conf import settings
import jwt


class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.user = SimpleLazyObject(lambda: self.__class__.get_jwt_user(request))

    @staticmethod
    def get_jwt_user(request):
        user_jwt = get_user(request)
        token = request.META.get('HTTP_AUTHORIZATION', None)
        if user_jwt.is_staff:
            return user_jwt
        else:
            user_jwt = AnonymousUser()
        if token is not None:
            try:
                user_jwt = jwt.decode(token[7:], settings.SECRET_KEY)
                user_jwt = User.objects.get(id=user_jwt['user_id'])
            except Exception as e:
                traceback.print_exc()

        return user_jwt

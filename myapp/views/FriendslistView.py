from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response

from myapp.models.UserModel import User
from myapp.serializers import FriendslistSerializer


class FriendslistViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    def list(self, request):

        queryset = User.objects.filter(friends__id=request.user.id)
        serializer = FriendslistSerializer(queryset, many=True)
        return Response([{"user": request.user.id}]+serializer.data)

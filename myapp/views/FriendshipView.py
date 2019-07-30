from django.db.models import Q

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets

from myapp.serializers import FriendshipSerializer
from myapp.models.UserModel import User
from myapp.models.FriendshipModel import Friendship


class FriendshipViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = Friendship.objects.filter(Q(request_owner=request.user.id) |
                                             Q(request_target=request.user.id))

        serializer = FriendshipSerializer(queryset, many=True)

        return Response([{"user": request.user.id}]+serializer.data)

    def create(self, request):
        if len(Friendship.objects.filter(request_owner=request.user.id,
                                         request_target=request.data["request_target"])) > 0:
            return Response(status=status.HTTP_409_CONFLICT)

        # if User already in friendslist
        if User.objects.get(id=request.data["request_target"]).friends.filter(id=request.user.id).exists():
            return Response(status=status.HTTP_409_CONFLICT)

        serializer = FriendshipSerializer(data={
            "request_owner": request.user.id,
            "request_target": request.data["request_target"]})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

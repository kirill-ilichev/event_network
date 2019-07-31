from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from myapp.models.EventModel import Event
from myapp.models.UserModel import User
from myapp.serializers import EventSerializer, EventListSerializer, UserSerializer
from myapp.permissions.IsOwnerOrReadOnly import IsOwnerOrReadOnly


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        is_mine = request.query_params.get('is_mine')
        if not is_mine or is_mine != "true":
            queryset = Event.objects.all()
        else:
            queryset = Event.objects.filter(author=self.request.user.id)
        serializer = EventListSerializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request):
        request.data["members"] = [request.user.id]
        request.data["author"] = request.user.id

        serializer = EventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_model = User.objects.get(id=request.user.id)
        user_model.events.add(serializer.data["id"])

        serializer = UserSerializer(user_model,
                                    data={"events": [event.id for event in user_model.events.all()]},
                                    partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
        return super(EventViewSet, self).get_permissions()

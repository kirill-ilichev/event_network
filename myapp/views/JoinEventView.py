from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from myapp.serializers import EventSerializer, UserSerializer
from myapp.models.EventModel import Event
from myapp.models.UserModel import User


class JoinEventView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):

        if request.data["join"]:
            event_model = Event.objects.get(id=pk)
            event_model.members.add(request.user.id)

            serializer = EventSerializer(event_model,
                                         data={"members": [member.id for member in event_model.members.all()]},
                                         partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            user_model = User.objects.get(id=request.user.id)
            user_model.events.add(event_model.id)

            serializer = UserSerializer(user_model,
                                        data={"events": [event for event in user_model.events.all()]},
                                        partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from myapp.serializers import UserSerializer
from myapp.models.UserModel import User
from myapp.models.FriendshipModel import Friendship


class FriendshipAcceptView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):
        if not Friendship.objects.filter(id=pk, request_target=request.user.id).exists():
            return Response(status=status.HTTP_404_NOT_FOUND)

        friendship_model = Friendship.objects.get(id=pk)

        if request.data["accept"]:
            friendship_addresser_id = friendship_model.request_owner
            user_model = User.objects.get(id=request.user.id)
            user_model.friends.add(friendship_addresser_id)
            serializer = UserSerializer(user_model,
                                        data={"friends": [friend.id for friend in user_model.friends.all()]},
                                        partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            friendship_model.delete()
        else:
            friendship_model.delete()

        return Response(status=status.HTTP_200_OK)

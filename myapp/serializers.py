from rest_framework import serializers

from django.contrib.auth import get_user_model

from myapp.models.FriendshipModel import Friendship
from myapp.models.EventModel import Event
from myapp.models.CommentModel import Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = get_user_model()
        fields = ('id', 'email', 'password', "city", "name", "friends")
        extra_kwargs = {'password': {'write_only': True}, }


class FriendshipSerializer(serializers.ModelSerializer):
    class Meta():
        model = Friendship
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    class Meta():
        model = Event
        fields = "__all__"


class EventListSerializer(serializers.ModelSerializer):
    class Meta():
        model = Event
        fields = ('title', 'text', 'date', 'id')


class FriendslistSerializer(serializers.ModelSerializer):
    class Meta():
        model = get_user_model()
        fields = ('id', 'name', 'city')


class CommentSerializer(serializers.ModelSerializer):
    class Meta():
        model = Comment
        fields = "__all__"

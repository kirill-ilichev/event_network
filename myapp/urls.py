from django.urls import path
from rest_framework.routers import DefaultRouter

from myapp.views.FriendshipView import FriendshipViewSet
from myapp.views.FriendslistView import FriendslistViewSet
from myapp.views.EventView import EventViewSet
from myapp.views.CommentView import CommentViewSet

from myapp.views.FriendshipAcceptView import FriendshipAcceptView
from myapp.views.JoinEventView import JoinEventView


urlpatterns = [
    path('friendship/<int:pk>/', FriendshipAcceptView.as_view()),
    path('event/<int:pk>/join/', JoinEventView.as_view()),
]

router = DefaultRouter()

router.register(r'event', EventViewSet)
urlpatterns += router.urls

router.register(r'friendship', FriendshipViewSet, base_name="friendship")
urlpatterns += router.urls

router.register(r'friendslist', FriendslistViewSet, base_name="friendslist")
urlpatterns += router.urls

router.register(r'comment', CommentViewSet, base_name='comment')
urlpatterns += router.urls

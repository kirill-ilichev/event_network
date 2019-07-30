from django.contrib import admin

from myapp.models.UserModel import User
from myapp.models.EventModel import Event
from myapp.models.CommentModel import Comment
from myapp.models.FriendshipModel import Friendship


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'id', 'city', 'name')


class FriendshipAdmin(admin.ModelAdmin):
    list_display = ('request_owner', 'request_target', 'id')


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'author')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'id', 'author')


admin.site.register(Friendship, FriendshipAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Comment, CommentAdmin)

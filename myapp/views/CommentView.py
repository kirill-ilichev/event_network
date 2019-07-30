from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from myapp.serializers import CommentSerializer
from myapp.models.CommentModel import Comment
from myapp.permissions.IsOwnerOrReadOnly import IsOwnerOrReadOnly


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def create(self, request):
        try:
            comment_model = Comment.objects.get(id=request.data['reply'])
            if not comment_model.is_tread:
                serializer = CommentSerializer(data={
                    'text': request.data['text'],
                    'author': request.user.id,
                    'is_tread': True,
                    'event': comment_model.event.id,
                    'reply': comment_model.id
                })
            else:
                return Response('You can\'t reply the reply', status=status.HTTP_403_FORBIDDEN)

        except KeyError:
            serializer = CommentSerializer(data={
                'text': request.data['text'],
                'author': request.user.id,
                'event': request.data['event']
            })
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
        return super(CommentViewSet, self).get_permissions()

    def get_queryset(self):
        event = self.request.query_params.get('event')
        if not event:
            queryset = Comment.objects.all()
        else:
            queryset = Comment.objects.filter(event=event)

        return queryset


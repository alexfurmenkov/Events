import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from events.models import Post, Person
from events.serializers import PostSerializer, SavePostSerializer
from events.responses import (
    ResponseAlreadyExists,
    ResponseCreated,
    ResponseNotFound
)
from events.decorators import request_validation


class PostHandler(APIView):
    """
    Class based view to handle authenticated requests
    on URL "/posts/"
    """
    permission_classes = [IsAuthenticated]
    authentication_class = JSONWebTokenAuthentication

    @classmethod
    def get(cls, request) -> Response:
        """
        Gets all posts of a current user
        :param request: GET HTTP request
        :return: JSON Response with serialized posts
        """
        posts = Post.objects.filter(author_id=request.user.id)
        serializer = PostSerializer(instance=posts, many=True)
        if not serializer.data:
            return ResponseNotFound('You have no posts')
        return Response(serializer.data, status=HTTP_200_OK)

    @classmethod
    @request_validation(SavePostSerializer)
    def post(cls, request) -> Response:
        """
        Saves new post to DB if it hasn't been saved before
        :param request: POST HTTP Request with new post details
                        in body, e.g. {'type': 'call', ...}
        :return: JSON Response with new post details
        """
        data = request.data
        user = Person.objects.get(id=request.user.id)

        if Post.get_event_by_contents(data['contents'], user.id):
            return ResponseAlreadyExists('Event with such content already exists')
        Post.objects.create(
                author=user,
                header=data['header'],
                contents=data['contents'],
                date=datetime.datetime.strptime(data['date'], '%Y-%m-%d %H:%M')
        )
        return ResponseCreated('New event is created')

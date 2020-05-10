from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from events.models import Post
from events.serializers import PostSerializer
from events.responses import ResponseNotFound


class PostsFilteredHandler(APIView):
    """
    Class based view to handle authenticated requests
    on URL "/posts/find/"
    """
    permission_classes = [IsAuthenticated]
    authentication_class = JSONWebTokenAuthentication

    @classmethod
    def get(cls, request) -> Response:
        """
        Gets all posts URL filtered
        :param request: GET HTTP request with params in URL, e.g.
                        "/posts/find/?header=call&time_period=week"
        :return: JSON Response with serialized post information
        """
        posts = Post.get_events_by_filters(
            data=request.query_params,
            author_id=request.user.id
        )
        if not posts:
            return ResponseNotFound(
                'Posts with such parameters are not found'
            )
        serializer = PostSerializer(
            instance=posts,
            many=True
        )
        return Response(serializer.data, status=HTTP_200_OK)

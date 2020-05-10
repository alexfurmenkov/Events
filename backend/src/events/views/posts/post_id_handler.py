from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from events.models import Post
from events.serializers import PostSerializer, EditPostSerializer
from events.utils import ResponseNotFound, ResponseSuccess


class PostByIdHandler(APIView):
    """
    Class based view to handle authenticated requests
    on URL "/posts/<post_id>/"
    """
    permission_classes = [IsAuthenticated]
    authentication_class = JSONWebTokenAuthentication

    @classmethod
    def get(cls, request, post_id) -> Response:
        """
        Gets post by id given in URL
        :param post_id: Post id
        :param request: GET HTTP request
        :return: JSON Response with serialized post information
        """
        post = Post.get_event_by_id(event_id=post_id)

        if post:
            serializer = PostSerializer(instance=post)
        else:
            return ResponseNotFound('Post with such id is not found')
        return Response(serializer.data, status=HTTP_200_OK)

    @classmethod
    def put(cls, request, post_id) -> Response:
        """
        Edits details of existing post
        :param post_id: Post id
        :param request: PUT HTTP Request with desired details
                        in body,
                        e.g. {'header': 'Dinner with ALex', ...}
        :return: JSON Response with updated details
        """
        post = Post.get_event_by_id(event_id=post_id)
        serializer = EditPostSerializer(request.data)
        return Response(
            {**post.update_attribute(
                serializer.run_validation(serializer.data)
            )},
            status=HTTP_200_OK
        )

    @classmethod
    def delete(cls, request, post_id) -> Response:
        """
        Deletes post
        :param post_id: Post id
        :param request: DELETE HTTP Request
        :return: JSON Response with deleted post details
        """
        post = Post.get_event_by_id(event_id=post_id)

        if post:
            post.delete()
        else:
            return ResponseNotFound('Post with such id is not found')
        return ResponseSuccess(
            f'Event {post.header} is deleted'
        )

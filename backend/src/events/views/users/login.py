from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from events.models import Person
from events.responses import ResponseNotFound, ResponseLogin
from events.decorators import request_validation
from events.serializers import LoginSerializer


class Login(APIView):
    """
    Class based view to handle any requests
    on URL "/users/login/"
    """
    permission_classes = (AllowAny,)

    @classmethod
    @request_validation(LoginSerializer)
    def post(cls, request):
        """
        Logs user in if username and password are correct
        :param request: POST HTTP request with user details
                        in body, e.g. {'email': 1, 'password': 1}
        :return: JSON Response with success or fail
        """
        user = Person.authenticate_user(
            request.data['email'],
            request.data['password']
        )
        if user is None:
            return ResponseNotFound(
                'User with such credentials is not found'
            )
        jwt_token = user.generate_jwt_token()
        return ResponseLogin(jwt_token)

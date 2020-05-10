from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from events.models import Person
from events.decorators import request_validation
from events.serializers import SignupSerializer
from events.responses import ResponseCreated, ResponseAlreadyExists


class SignUp(APIView):
    """
    Class based view to handle any requests
    on URL "/users/signup/"
    """
    permission_classes = (AllowAny,)

    @classmethod
    @request_validation(SignupSerializer)
    def post(cls, request):
        """
        Registers new user if he was not registered before
        :param request: POST HTTP request with user details in body,
                        e.g. {'email': 'alexfurm@mail.ru', ...}
        :return: JSON Response with redirect link to the login page
        """
        data = request.data

        if Person.get_user_by_email(data['email']):
            return ResponseAlreadyExists(
                'Such email already exists'
            )
        Person.objects.create(
            email=data['email'],
            password=Person.hash_password_with_salt(
                data['password']
            )
        )
        return ResponseCreated('New user is saved')

"""
Response with status HTTP_200_OK
when user is successfully logged in
Returns JWT token
"""
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class ResponseLogin(Response):
    """
    Response class
    """
    def __init__(self, token):
        super().__init__(status=HTTP_200_OK)
        self.data = dict(
            status='success',
            token=token,
        )

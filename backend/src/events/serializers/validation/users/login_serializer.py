from rest_framework.serializers import (
    Serializer,
    CharField,
    EmailField
)


class LoginSerializer(Serializer):
    """
    Serializer class
    """
    email = EmailField(required=True, label='email', max_length=512)
    password = CharField(required=True, label='password',
                         max_length=512, min_length=6)

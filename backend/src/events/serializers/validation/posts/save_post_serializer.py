from rest_framework.serializers import (
    Serializer,
    CharField
)


class SavePostSerializer(Serializer):
    """
    Serializer class
    """
    header = CharField(required=True, label='header', max_length=512)
    contents = CharField(required=True, label='contents',
                         max_length=10000)
    date = CharField(required=True, label='date', max_length=512)

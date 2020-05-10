from rest_framework.serializers import (
    Serializer,
    CharField,
)


class EditPostSerializer(Serializer):
    """
    Serializer class
    """
    header = CharField(required=False, label='header', max_length=512)
    contents = CharField(required=False, label='contents',
                         max_length=10000)
    date = CharField(required=False, label='date', max_length=512)

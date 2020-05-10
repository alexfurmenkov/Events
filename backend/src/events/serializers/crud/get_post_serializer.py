from rest_framework.serializers import ModelSerializer
from events.models import Post


class PostSerializer(ModelSerializer):
    """
    Serializer class
    """
    class Meta:
        model = Post
        fields = ['id',
                  'header',
                  'contents',
                  'date',
                  ]

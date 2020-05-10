import datetime

from django.db import models

from .person import Person


class Post(models.Model):
    """
    Post model
    """
    class Meta:
        app_label = 'events'

    author = models.ForeignKey(Person, default=None,
                               on_delete=models.CASCADE)
    header = models.CharField(max_length=512, default=None)
    contents = models.TextField(max_length=10000, default=None)
    date = models.DateTimeField()

    @classmethod
    def get_event_by_id(cls, event_id):
        """
        Gets event by id
        :param event_id: id of any Post object
        :return: Post object if it exists,
                 if not - returns False
        """
        try:
            existing_event = cls.objects.get(id=event_id)
            return existing_event
        except cls.DoesNotExist:
            return None

    @classmethod
    def get_event_by_contents(cls, contents, author_id):
        """
        Gets event by content and author_id
        :param author_id: id of the User object
        :param contents: contents of the Post object
        :return: Post object with corresponding contents
        """
        try:
            existing_event = cls.objects.get(
                contents=contents,
                author_id=author_id
            )
        except cls.DoesNotExist:
            return None
        return existing_event

    @classmethod
    def get_events_by_header(cls, header, author_id):
        """
        Gets event by header and author_id
        :param author_id: id of the User object
        :param header: header of the Post object
        :return: Post object with corresponding contents
        """
        posts = cls.objects.filter(
            author_id=author_id,
            header=header
        )
        if not posts:
            return None
        return posts

    @classmethod
    def get_events_by_time(cls, time_period, author_id):
        """
        Gets event by time and author_id
        :param author_id: id of the User object
        :param time_period: difference between the time of creation
                            of the Post object and now
        :return: Post object with corresponding contents
        """
        posts = None
        if time_period == 'day':
            posts = cls.objects.filter(
                author_id=author_id,
                date__range=[
                    datetime.date.today(),
                    datetime.date.today() + datetime.timedelta(days=1)
                ]
            )
        elif time_period == 'week':
            posts = cls.objects.filter(
                author_id=author_id,
                date__range=[
                    datetime.date.today(),
                    datetime.date.today() + datetime.timedelta(days=7)
                ]
            )
        elif time_period == 'month':
            posts = cls.objects.filter(
                author_id=author_id,
                date__range=[
                    datetime.date.today(),
                    datetime.date.today() + datetime.timedelta(weeks=4)
                ]
            )
        if not posts:
            return None
        return posts

    @classmethod
    def get_events_by_filters(cls, data, author_id):
        """
        Gets post by filters
        :param author_id: id of User object
        :param data: dictionary with filters
        :return: All Post objects
                 corresponding to the filters
        """
        posts = None
        if 'header' in data and 'time_period' not in data:
            posts = cls.get_events_by_header(
                data['header'],
                author_id
            )
        elif 'time_period' in data and 'header' not in data:
            posts = cls.get_events_by_time(
                data['time_period'],
                author_id
            )
        elif 'header' in data and 'time_period' in data:
            posts = cls.get_events_by_time(
                data['time_period'],
                author_id
            )
            if posts:
                posts = [post for post in posts if post.header == data['header']]
        if not posts:
            return None
        return posts

    def update_attribute(self, data):
        """
        Updates attribute of any Event object
        :param data: Dict with attributes to be updated
        :return: Dict with updated attributes
        """
        updated_attributes = {}

        for attribute, value in data.items():
            setattr(self, attribute, value)
            self.save()
            updated_attributes[attribute] = value

        return updated_attributes

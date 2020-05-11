from __future__ import absolute_import, unicode_literals

import datetime

from celery import shared_task

from django.core.mail import send_mail

from .models import Post


@shared_task
def hello():
    print('Starting to check if there are some upcoming events')
    current_timedate = datetime.datetime.now()

    for post in Post.objects.all():
        if post.date.date() == current_timedate.date() \
                and (post.date.hour - current_timedate.hour <= 1):
            send_mail(
                'Upcoming event',
                f'You have an upcoming event - {post.contents}',
                'worktestalexfurm@gmail.com',
                [post.author.email],
                fail_silently=False
            )
            print('Email has been sent')

from __future__ import absolute_import, unicode_literals

from celery.task import periodic_task

from datetime import timedelta


@periodic_task(run_every=(timedelta(seconds=8)), name='hello')
def hello():
    print('Hello there!')

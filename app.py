from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery import shared_task
import os

MQ_USER = os.environ.get("MQ_USER")
MQ_PWD = os.environ.get("MQ_PWD")
MQ_HOST = os.environ.get("MQ_HOST")

app = Celery(
    'app',
    broker='amqp://{}:{}@{}//'.format(MQ_USER, MQ_PWD, MQ_HOST),
)


@shared_task
def add(x, y):
    return x + y


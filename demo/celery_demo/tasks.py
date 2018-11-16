import time

from celery.task import Task


class DemoTask(Task):
    name = 'demo-task'

    def run(self, *args, **kwargs):
        print('start task')
        time.sleep(4)
        print(f'args: {args}, kwargs: {kwargs}')
        print('end task')


import time

from tasks import add
from celery_app import task1, task2


def celery1():
    print('start task')
    result = add.delay(2, 8)
    print(result)
    print('end task')

def celery2():
    print('start task')
    task1.add.delay(2, 4)
    task2.multiply.delay(4, 5)
    print('end task')


if __name__ == '__main__':
    # celery1()

    celery2()


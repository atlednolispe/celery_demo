from datetime import timedelta

import djcelery


djcelery.setup_loader()

# fangzhi renwu guoduo, gongyong moren queue
CELERY_QUEUES = {
    'beat_tasks': {
        'exchange': 'beat_tasks',
        'exchange_type': 'direct',
        'binding_key': 'beat_tasks',
    },
    'work_queue': {
        'exchange': 'work_queue',
        'exchange_type': 'direct',
        'binding_key': 'work_queue',
    },
}

CELERY_DEFAULT_QUEUE = 'work_queue'

CELERY_IMPORTS = (
    'celery_demo.tasks',
)


# youxieqingkuangfangzhi sisuo
CELERY_FORCE_EXECV = True

# bingfa worker num yiban = CPU shu
CELERY_CONCURRENCY = 4

# shibai yunxu chongshi
CELERY_ACKS_LATE = True

# meige worker zuiduo zhixing 100 ge renwu bei xiaohui, fangzhi neicun xielou
CELERYD_MAX_TASKS_PER_CHILD = 100

# chaoshi dange renwu zuida shijian, chaoguo bei kill
CELERYD_TASK_TIME_LIMIT = 12 * 30

CELERYBEAT_SCHEDULE = {
    'task1': {
        'task': 'demo-task',
        'schedule': timedelta(seconds=5),
        'args': (1, 2),
        'options': {
            'queue': 'beat_tasks',
        },
    }
}

# IMPORT TO DJANGO SETTINGS
BROKER_BACKEND = 'redis'
BROKER_URL = 'redis://localhost:6379/1'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'

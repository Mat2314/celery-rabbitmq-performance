from celery import Celery
from performance_project import celeryconfig
from celery.schedules import crontab

app = Celery('performance_project', broker='amqp://guest:guest@rabbitmq:5672', backend='rpc://',
             include=['performance_project.tasks'])

app.config_from_object(celeryconfig)

if __name__ == '__main__':
    app.start()

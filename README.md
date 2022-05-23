# Celery Rabbitmq performance issue
Repository contains code that causes rabbitmq crash when executing multiple heavy tasks by multiple celery workers.

## Hands on
In the root directory execute the following commands:
```
### Copy .env.example file to .env file
$ cp api/performance_project/.env.example api/performance_project/.env

### Spin up the containers 
$ docker-compose up
```

Now in a separate terminal tab or window:
```
### List running containers
$ docker ps

### Enter django project container
$ docker exec -it [django_container_id_here] bash

### Run python shell of the django project
(container) $ python3 manage.py shell

### Import task and queue many of them
>>> from performance_project.tasks import simulate_heavy_task
>>> for i in range(250):
...     simulate_heavy_task.delay()
```

Now take a look at containers' logs. 
After short time rabbitmq container should crash with the following message:

```
rabbitmq_1      | 2022-05-23 14:11:47.259407+00:00 [error] <0.1287.0>     supervisor: {<0.1287.0>,rabbit_channel_sup_sup}
rabbitmq_1      | 2022-05-23 14:11:47.259407+00:00 [error] <0.1287.0>     errorContext: shutdown_error
rabbitmq_1      | 2022-05-23 14:11:47.259407+00:00 [error] <0.1287.0>     reason: noproc
rabbitmq_1      | 2022-05-23 14:11:47.259407+00:00 [error] <0.1287.0>     offender: [{nb_children,1},
rabbitmq_1      | 2022-05-23 14:11:47.259407+00:00 [error] <0.1287.0>                {id,channel_sup},
rabbitmq_1      | 2022-05-23 14:11:47.259407+00:00 [error] <0.1287.0>                {mfargs,{rabbit_channel_sup,start_link,[]}},
rabbitmq_1      | 2022-05-23 14:11:47.259407+00:00 [error] <0.1287.0>                {restart_type,temporary},
rabbitmq_1      | 2022-05-23 14:11:47.259407+00:00 [error] <0.1287.0>                {shutdown,infinity},
rabbitmq_1      | 2022-05-23 14:11:47.259407+00:00 [error] <0.1287.0>                {child_type,supervisor}]

```


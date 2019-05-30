## Running With 
- python 3.6
- rabbitmq 3.7.12
- erlang 21.2.6

##Set The env First

### In windows
- set MQ_USER=your_mq_user
- set MQ_PWD=your_mq_password
- set MQ_HOST=your_mq_host

### In linux
- export MQ_USER=your_mq_user
- export MQ_PWD=your_mq_password
- export MQ_HOST=your_mq_host

### In dockerfile
- ENV MQ_USER your_mq_user
- ENV MQ_PWD your_mq_password
- ENV MQ_HOST your_mq_host

## Install requirements
- pip3 install -r requirements.txt

## Just run the workers
- celery -A app worker -l info -n demo001 -P eventlet --heartbeat-interval 60
- celery -A app worker -l info -n demo002 -P eventlet --heartbeat-interval 60
- celery -A app worker -l info -n demo003 -P eventlet --heartbeat-interval 60

## Finally just watch the worker logs and the rabbitMQ logs 
## 2 minutes (my rabbitmq default heartbeat is 120)

![MQ Miss The Worker](https://github.com/pytomtoto/celery-eventlet-cluster-test/blob/master/img/celery-rabbitmq.png)

![The Worker Error](https://github.com/pytomtoto/celery-eventlet-cluster-test/blob/master/img/celery-rabbitmq-ex.png)

![The MQ Logs](https://github.com/pytomtoto/celery-eventlet-cluster-test/blob/master/img/The-rabbitmq-log.png)


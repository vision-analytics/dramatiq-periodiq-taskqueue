# sample-taskqueue-dramatiq

Simple <b>dramatiq</b> task queue starter project.

<b>periodiq</b> is used for scheduled tasks.

## Getting started

```bash
docker-compose up --build
```

## Run a dummy task

```bash

docker exec -it sample-taskqueue-dramatiq-dramatiq-1 bash

./bin/execute_test_task.sh

# or

python3 -c "from dramatiq_taskqueue import tasks; tasks.test_task.send('test_input')"
python3 -c "from dramatiq_taskqueue import tasks; tasks.test_task_fail.send('test_input2')"
python3 -c "from dramatiq_taskqueue import tasks; tasks.test_task_fail2.send('test_input3')"

```

## Sample logs

```bash
sample-taskqueue-dramatiq-periodiq-1  | [2023-01-09 19:54:39,694] [PID 7] [MainThread] [periodiq] [INFO] Scheduling Actor(test_scheduled_task_1) at 2023-01-09T19:54:40+00:00.
sample-taskqueue-dramatiq-periodiq-1  | [2023-01-09 19:54:39,694] [PID 7] [MainThread] [dramatiq.broker.RedisBroker] [DEBUG] Enqueueing message '70ff2833-7699-44d7-8227-56e8c8ce011e' on queue 'default'.
sample-taskqueue-dramatiq-periodiq-1  | [2023-01-09 19:54:39,700] [PID 7] [MainThread] [periodiq] [DEBUG] Nothing to do until 2023-01-09T19:55:00+00:00.
sample-taskqueue-dramatiq-periodiq-1  | [2023-01-09 19:54:39,700] [PID 7] [MainThread] [periodiq] [DEBUG] Sleeping for 20s (<Period [2023-01-09T19:54:39.700209+00:00 -> 2023-01-09T19:55:00+00:00]>).
sample-taskqueue-dramatiq-dramatiq-1  | [2023-01-09 19:54:39,739] [PID 12] [Thread-4] [periodiq] [INFO] Processing 70ff2833-7699-44d7-8227-56e8c8ce011e:test_scheduled_task_1() scheduled at 2023-01-09T19:54:40+00:00.
sample-taskqueue-dramatiq-dramatiq-1  | [2023-01-09 19:54:39,739] [PID 12] [Thread-4] [dramatiq_taskqueue] [INFO] Running scheduled task #1 @01/09/2023, 19:54:39
sample-taskqueue-dramatiq-dramatiq-1  | [2023-01-09 19:54:59,317] [PID 12] [Thread-5] [dramatiq_taskqueue] [INFO] Running #test-task with param: test_input
sample-taskqueue-dramatiq-periodiq-1  | [2023-01-09 19:55:00,030] [PID 7] [MainThread] [periodiq] [DEBUG] Alaaaaarm!
sample-taskqueue-dramatiq-periodiq-1  | [2023-01-09 19:55:00,046] [PID 7] [MainThread] [periodiq] [DEBUG] Wake up at 2023-01-09T19:55:00+00:00.
sample-taskqueue-dramatiq-periodiq-1  | [2023-01-09 19:55:00,048] [PID 7] [MainThread] [periodiq] [INFO] Scheduling Actor(test_scheduled_task_1) at 2023-01-09T19:55:00+00:00.
sample-taskqueue-dramatiq-periodiq-1  | [2023-01-09 19:55:00,049] [PID 7] [MainThread] [dramatiq.broker.RedisBroker] [DEBUG] Enqueueing message 'fd181064-b7a6-402f-9309-3d722c822088' on queue 'default'.
sample-taskqueue-dramatiq-periodiq-1  | [2023-01-09 19:55:00,054] [PID 7] [MainThread] [periodiq] [INFO] Scheduling Actor(test_scheduled_task_2) at 2023-01-09T19:55:00+00:00.
sample-taskqueue-dramatiq-periodiq-1  | [2023-01-09 19:55:00,054] [PID 7] [MainThread] [dramatiq.broker.RedisBroker] [DEBUG] Enqueueing message 'd74639ce-547f-429f-91e6-8c07fcd861dd' on queue 'default'.
sample-taskqueue-dramatiq-periodiq-1  | [2023-01-09 19:55:00,057] [PID 7] [MainThread] [periodiq] [DEBUG] Nothing to do until 2023-01-09T19:56:00+00:00.
sample-taskqueue-dramatiq-periodiq-1  | [2023-01-09 19:55:00,058] [PID 7] [MainThread] [periodiq] [DEBUG] Sleeping for 59s (<Period [2023-01-09T19:55:00.057762+00:00 -> 2023-01-09T19:56:00+00:00]>).
sample-taskqueue-dramatiq-dramatiq-1  | [2023-01-09 19:55:00,131] [PID 15] [Thread-8] [periodiq] [INFO] Processing d74639ce-547f-429f-91e6-8c07fcd861dd:test_scheduled_task_2() scheduled at 2023-01-09T19:55:00+00:00.
sample-taskqueue-dramatiq-dramatiq-1  | [2023-01-09 19:55:00,132] [PID 15] [Thread-8] [dramatiq_taskqueue] [INFO] Running scheduled task #2 @01/09/2023, 19:55:00
sample-taskqueue-dramatiq-dramatiq-1  | [2023-01-09 19:55:00,136] [PID 15] [Thread-10] [periodiq] [INFO] Processing fd181064-b7a6-402f-9309-3d722c822088:test_scheduled_task_1() scheduled at 2023-01-09T19:55:00+00:00.
sample-taskqueue-dramatiq-dramatiq-1  | [2023-01-09 19:55:00,136] [PID 15] [Thread-10] [dramatiq_taskqueue] [INFO] Running scheduled task #1 @01/09/2023, 19:55:00
```

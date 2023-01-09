# sample-taskqueue-dramatiq

Sample <b>dramatiq</b> task queue setup.

<b>periodiq</b> is used for scheduled tasks.

## Getting Started


```bash
docker-compose up --build
```

## run a test task


```bash

docker exec -it sample-taskqueue-dramatiq-dramatiq-1 bash

./bin/execute_test_task.sh

# or

python3 -c "from dramatiq_taskqueue import tasks; tasks.test_task.send('test_input')"
python3 -c "from dramatiq_taskqueue import tasks; tasks.test_task_always_fail.send('test_input')"

```

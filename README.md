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
python3 -c "from dramatiq_taskqueue import tasks; tasks.test_task_always_fail.send('test_input')"

```

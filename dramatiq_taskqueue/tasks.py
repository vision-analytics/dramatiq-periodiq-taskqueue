import dramatiq
from dramatiq_taskqueue import MAX_RETRIES, logger, should_retry
from dramatiq_taskqueue.scheduled_tasks import *


@dramatiq.actor()
def handle_task_failure(message_data, exception_data):
    """Actor to handle task failures."""
    actor_name = message_data["actor_name"]
    task_args = message_data["args"]
    retries = message_data["options"]["retries"] - 1
    if retries >= MAX_RETRIES:
        logger.warning(
            f"Retries({retries}) exceeded for the actor {actor_name} with args {task_args}"
        )
    else:
        logger.info(
            f"The actor {actor_name} with args {task_args} will be retried "
            + f"{MAX_RETRIES-retries} more times. retries:{retries} - max_retries:{MAX_RETRIES}"
        )


@dramatiq.actor(max_retries=MAX_RETRIES)
def test_task(param1: str) -> None:
    """Dummy task."""
    logger.info(f"Running #test-task with param: {param1}")


@dramatiq.actor(max_retries=MAX_RETRIES)
def test_task_fail(param1: str) -> None:
    """Dummy task that always fails."""
    logger.info(f"Running #test-task (fail) with param: {param1}")
    raise Exception("unable to run task")


@dramatiq.actor(retry_when=should_retry)
def test_task_fail2(param1: str) -> None:
    """Dummy task that always fails."""
    logger.info(f"Running #test-task (fail) with param: {param1}")
    raise Exception("unable to run task")

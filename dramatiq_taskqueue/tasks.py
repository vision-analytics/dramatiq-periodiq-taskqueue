import dramatiq
from dramatiq_taskqueue import logger
from dramatiq_taskqueue.scheduled_tasks import *

@dramatiq.actor()
def test_task(param1: str) -> None:
    """Dummy task."""
    logger.info(f"Running #test-task with param: {param1}")

@dramatiq.actor()
def test_task_fail(param1: str) -> None:
    """Dummy task that always fails."""
    logger.info(f"Running #test-task (fail) with param: {param1}")
    raise Exception("unable to run task")

import dramatiq
from dramatiq_taskqueue import logger
from dramatiq_taskqueue.scheduled_tasks import *

@dramatiq.actor()
def test_task(param1: str) -> None:
    logger.info(f"Running #test-task with param: {param1}")

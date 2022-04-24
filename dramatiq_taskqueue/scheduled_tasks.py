from datetime import datetime

import dramatiq
from dramatiq_taskqueue import logger
from periodiq import PeriodiqMiddleware, cron

def get_timestamp() -> str:
    return datetime.now().strftime("%m/%d/%Y, %H:%M:%S")


@dramatiq.actor(periodic=cron("* * * * *"))
def test_scheduled_task_1():
    logger.info(f"Running scheduled task #1 @{get_timestamp()}")


@dramatiq.actor(periodic=cron("*/5 * * * *"))
def test_scheduled_task_2():
    logger.info(f"Running scheduled task #2 @{get_timestamp()}")

import logging

import bjoern
import dramatiq
from dramatiq.brokers.redis import RedisBroker
from dramatiq_dashboard import DashboardApp
from periodiq import PeriodiqMiddleware


logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

MAX_RETRIES = 2

redis_broker = RedisBroker(host="redis")
redis_broker.add_middleware(PeriodiqMiddleware(skip_delay=30))

dramatiq.set_broker(redis_broker)


def should_retry(retries_so_far, exception):
    return retries_so_far < MAX_RETRIES and isinstance(exception, Exception)


# app = DashboardApp(broker=redis_broker, prefix="")
# bjoern.run(app, "127.0.0.1", 5001)

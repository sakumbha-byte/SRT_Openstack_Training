from oslo_service import service
from oslo_log import log as logging
from myservice.config import CONF

LOG = logging.getLogger(__name__)

class MyService(service.Service):

    def start(self):
        super().start()

        LOG.info("Service started with interval %s",
                 CONF.periodic_interval)

        self.tg.add_timer(
            CONF.periodic_interval,
            self.periodic_task
        )

    def periodic_task(self):
        LOG.info("Running periodic task")

    def stop(self):
        LOG.info("Service stopping")
        super().stop()

from oslo_service import service, loopingcall
import time

class Myservice(service.Service):
    
    def start(self):
        super().start()
        print("Service Started")

        self.tg.add_timer(
                5,
                self.periodic_task
        )

    def periodic_task(self):
        print("Running periodic task", time.ctime())

    def stop(self):
        print("Service stopping")
        super().stop()

from datetime import datetime
import os

from st2reactor.sensor.base import PollingSensor


class CounterSensor(PollingSensor):

    def __init__(self, sensor_service, config,
                 poll_interval=60):
        super(CounterSensor, self).__init__(
            sensor_service=sensor_service,
            config=config,
            poll_interval=poll_interval
        )
        self.count = None
        self.logger = None

    def setup(self):
        self.count = 1
        self.logger = self.sensor_service.get_logger(name=self.__class__.__name__)

    def poll(self):
        cmd = 'date'
        payload = {
            "count": self.count,
            "pythonpath": os.environ.get("PYTHONPATH", None),
            "name": "chao",
            "cmd": cmd
          }
        currTime = str(datetime.now())
        # version = mymain.VERSION
        info = "############## healing, cmd: {cmd}, time: {currTime}, count: {count}, payload: {payload}".format(
            cmd=cmd,
            currTime=currTime,
            count=self.count,
            payload=payload,
        )

        self.logger.info(info)

        # NOTE, must add below code to send data which is used to valid rule
        self.sensor_service.dispatch(trigger="healing.counter", payload=payload)
        self.count = self.count + 1

    def cleanup(self):
        pass

    def add_trigger(self, trigger):
        # This method is called when trigger is created
        pass

    def update_trigger(self, trigger):
        # This method is called when trigger is updated
        pass

    def remove_trigger(self, trigger):
        # This method is called when trigger is deleted
        pass
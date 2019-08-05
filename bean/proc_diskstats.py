import time


class DiskStatsBean(object):
    def __init__(self, device_id, sub_id, device_name, io_times):
        self.device_id = device_id
        self.sub_id = sub_id
        self.device_name = device_name
        self.io_times = int(io_times)
        self.occupy = -1
        self.now = time.time()

    def set_disk_occupy(self, beanpre):
        if beanpre:
            io_time_delta = self.io_times - beanpre.io_times
            self.occupy = float(io_time_delta) / (self.now - beanpre.now)
        else:
            pass

    def __str__(self):
        return "%s: %0.2f" \
               % (self.device_name, self.occupy)

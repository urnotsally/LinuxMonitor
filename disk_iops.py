import time
from bean.proc_diskstats import DiskStatsBean

FILEPATH = "/proc/diskstats"
INTERVALS = 500  # ms


def _get_disk_dict():
    """ Return the information of first line in /proc/stat
    as a dictionary in the following format:
    """
    disk_dict = {}
    with open(FILEPATH) as f:
        for line in f:
            data = line.strip().split()
            disk_bean = DiskStatsBean(data[0], data[1], data[2], data[12])
            disk_dict[disk_bean.device_name] = disk_bean
    return disk_dict


def get_disks_occupy():
    disk_pre = _get_disk_dict()
    time.sleep(INTERVALS / 1000.0)
    disk_cur = _get_disk_dict()
    for keys in disk_pre:
        disk_cur[keys].set_disk_occupy(disk_pre[keys])
    return disk_cur.values()

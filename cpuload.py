from bean.proc_loadavg import LoadAvgBean

FILEPATH = "/proc/loadavg"


def _get_cpu():
    """ Return the information of first line in /proc/stat
    as a dictionary in the following format:
    """
    with open(FILEPATH) as f:
        cpu_load = f.readline().strip().split()
    return LoadAvgBean(cpu_load[:3])


def get_loadavg():
    return _get_cpu().get_load()

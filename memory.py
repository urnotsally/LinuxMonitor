from itertools import islice
from bean.proc_meminfo import MemInfoBean

FILEPATH = "/proc/meminfo"


def _get_mem():
    """ Return the information in /proc/meminfo
    as a dictionary in the following format:
    """
    mem_dict = {}
    with open(FILEPATH) as f:
        for line in islice(f, None, 5):
            item = line.strip().lower().split(":")
            mem_dict[item[0]] = item[1][:-3]
    return MemInfoBean(**mem_dict)


def get_mem_occupy():
    return _get_mem().get_occupy()

from itertools import islice
from collections import namedtuple

FILEPATH = "/proc/meminfo"
mem_ntuple = namedtuple('mem', 'memtotal, memfree, memavailable, cached, buffers')


def _get_mem():

    mem_dict = {}
    with open(FILEPATH) as f:
        for line in islice(f, None, 5):
            item = line.strip().lower().split(":")
            mem_dict[item[0]] = int(item[1][:-3])
    return mem_ntuple(**mem_dict)


def get_mem_occupy():
    memory = _get_mem()
    used = memory.memtotal - memory.memavailable
    occupy = round(float(used) / memory.memtotal, 2)
    return occupy

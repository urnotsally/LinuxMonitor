from collections import namedtuple

FILEPATH = "/proc/loadavg"
load_ntuple = namedtuple('cpu_load', 'one five fifteen')


def get_cpu_load():

    with open(FILEPATH) as f:
        cpu_load = f.readline().strip().split()
    return load_ntuple(cpu_load[0], cpu_load[1], cpu_load[2])

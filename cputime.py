import time
from bean.proc_stat import StatBean

FILEPATH = "/proc/stat"
INTERVALS = 0.5  # s


def _get_cpu():
    with open(FILEPATH) as f:
        total_cpu = f.readline().strip().split()
    total_cpu.remove(total_cpu[0])
    cpu_info = StatBean(total_cpu)
    return cpu_info


def get_cpu_occupy():
    pre_cpu = _get_cpu()
    time.sleep(INTERVALS)
    cpu = _get_cpu()
    total_delta = cpu.get_total() - pre_cpu.get_total()
    if total_delta > 0:
        active_delta = cpu.get_active() - pre_cpu.get_active()
        occupy = float(active_delta) / total_delta * 100
        return occupy
    elif total_delta <= 0:
        return 0

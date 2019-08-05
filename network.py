import time
from bean.proc_netdev import NetDevBean

FILEPATH = "/proc/net/dev"
INTERVALS = 500  # ms


def _get_eth_dict():
    """ Return the information of first line in /proc/stat
    as a dictionary in the following format:
    """
    eth_dict = {}
    with open(FILEPATH) as f:
        for line in f:
            item = line.strip().split(":")
            if item[0].startswith("eth"):
                data = item[1].split()
                ethbean = NetDevBean(item[0], data[0], data[8])
                eth_dict[ethbean.interface] = ethbean
            else:
                continue
    return eth_dict


def get_net_rate():
    ethpre = _get_eth_dict()
    time.sleep(500/1000.0)
    ethcur = _get_eth_dict()
    for keys in ethcur:
        ethcur[keys].set_rate(ethpre[keys])
    return ethcur.values()

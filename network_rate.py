import time
from collections import namedtuple

FILEPATH = "/proc/net/dev"
INTERVALS = 500  # ms
net_ntuple = namedtuple('net', 'interface, recv_bytes, transmit_bytes, time')
rate_ntuple = namedtuple('net_rate', 'interface, recv_rate, transmit_rate')


def _get_eth_dict():
    eth_dict = {}
    with open(FILEPATH) as f:
        for line in f:
            item = line.strip().split(":")
            if item[0].startswith("eth"):
                data = item[1].split()
                eth_bean = net_ntuple(item[0], float(data[0]), float(data[8]), time.time())
                eth_dict[eth_bean.interface] = eth_bean
            else:
                continue
    return eth_dict


def get_net_rate():
    eth_dict_pre = _get_eth_dict()
    time.sleep(0.5)
    eth_dict_cur = _get_eth_dict()
    res_list = []
    for key in eth_dict_cur:
        if key in eth_dict_pre:
            eth_pre = eth_dict_pre[key]
            eth_cur = eth_dict_cur[key]
            recv_rate = (eth_cur.recv_bytes - eth_pre.recv_bytes) / ((eth_cur.time - eth_pre.time) * 0.001)
            transmit_bytes = (eth_cur.transmit_bytes - eth_pre.transmit_bytes) / ((eth_cur.time - eth_pre.time) * 0.001)
            item = rate_ntuple(key, round(recv_rate, 2), round(transmit_bytes, 2))
            res_list.append(item)
    return res_list

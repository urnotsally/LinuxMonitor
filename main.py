#!/usr/bin/env Python
from cputime import *
from memory import *
from cpuload import *
from disk import *
from network import *


if __name__ == '__main__':
    while True:
        localtime = time.asctime(time.localtime(time.time()))
        print(localtime + "-----------------------------")
        print(r'% ' + "cpu : %f" % get_cpu_occupy())
        print(r'% ' + "mem : %f" % get_mem_occupy())
        print("cpu_load[1m 5m 15m]:" + get_loadavg())
        for item in get_disks_occupy():
            print(item)
        for item in get_net_rate():
            print(item)
        time.sleep(20)

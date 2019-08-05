#!/usr/bin/env Python
import cpu_occupy
import memory_occupy
import cpu_load
from disk_iops import *
from network_rate import *
import disk_usage

if __name__ == '__main__':
    while True:
        localtime = time.asctime(time.localtime(time.time()))
        print(localtime + "-----------------------------")
        print "[cpu_occupy] "+r'% '+": %.2f" % cpu_occupy.get_cpu_occupy()
        print "[memory_occupy]"+r' % '+": %.2f" % memory_occupy.get_mem_occupy()
        load = cpu_load.get_cpu_load()
        print "[cpu_load] %s %s %s" % (load.one, load.five, load.fifteen)
        for item in get_net_rate():
            print "[%s] receive: %.2f KB/S ; transmit: %.2f KB/S" % (item.interface, item.recv_rate, item.transmit_rate)
        for dev in disk_usage.disk_partitions():
            usage = disk_usage.disk_usage(dev.mountpoint)
            print "[%s] used" % dev.device + r' %' + ":  %.1f " % usage.percent
        time.sleep(20)
#!/usr/bin/env Python
import time
import cpu_occupy
import memory_occupy
import cpu_load
import network_rate
import disk_usage

if __name__ == '__main__':
    while True:
        localtime = time.asctime(time.localtime(time.time()))
        print(localtime + "-----------------------------")
        print "[cpu_occupy] "+": %.2f" % cpu_occupy.get_cpu_occupy() + r' %'
        print "[memory_occupy]"+": %.2f" % memory_occupy.get_mem_occupy()+r' %'
        load = cpu_load.get_cpu_load()
        print "[cpu_load] 1min 5min 15mim: %s %s %s" % (load.one, load.five, load.fifteen)
        print "[network_speed]"
        for item in network_rate.get_net_rate():
            print "%s recv: %.2f Kb/s ; trans: %.2f Kb/s" % (item.interface, item.recv_rate, item.transmit_rate)
        print "[disk_usage]"
        for dev in disk_usage.disk_partitions():
            usage = disk_usage.disk_usage(dev.mountpoint)
            print "%s" % dev.device + ":  %.1f " % usage.percent + r' %'
        time.sleep(30)

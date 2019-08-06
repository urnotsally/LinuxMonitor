import time


class NetDevBean:
    def __init__(self, interface, receive_bytes, transmit_bytes):
        self.interface = interface
        self.recv_bytes = float(receive_bytes)
        self.send_bytes = float(transmit_bytes)
        self.recv_rate = -1
        self.send_rate = -1
        self.now = time.time()

    def set_rate(self, bean_pre):
        recv_rate = (self.recv_bytes - bean_pre.recv_bytes) / ((self.now - bean_pre.now) * 0.001)
        send_rate = (self.send_bytes - bean_pre.send_bytes) / ((self.now - bean_pre.now) * 0.001)
        self.recv_rate = recv_rate
        self.send_rate = send_rate
        return self

    def __str__(self):
        return "%s: receive_rate: %0.2f Byte/s; send_rate: %0.2f Byte/s" \
               % (self.interface, self.recv_rate, self.send_rate)

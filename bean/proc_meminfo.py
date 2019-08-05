class MemInfoBean:
    def __init__(self, memtotal, memfree, memavailable, cached, buffers):
        self.total = int(memtotal)
        self.available = int(memavailable)
        self.free = int(memfree)
        self.cached = int(cached)
        self.buffers = int(buffers)

    def get_used(self):
        return self.total - self.available

    def get_occupy(self):
        return float(self.get_used()) / self.total

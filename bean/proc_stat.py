class StatBean:
    """ OccupyTime of Cpu
        only record the first five fields
    """

    def __init__(self, args):
        attrs = ["user", "nice", "system", "idle", "io_wait", "irq", "soft_irq", "steal", "guest", "guest_nice"]
        args = map(int, args)
        for i in range(len(args)):
            setattr(self, attrs[i], args[i])

    def get_total(self):
        total = 0
        for value in vars(self).values():
            total += value
        return total

    def get_active(self):
        return self.get_total() - self.idle

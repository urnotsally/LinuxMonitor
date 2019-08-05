class LoadAvgBean:
    def __init__(self, args):
        attrs = ["lavg1", "lavg5", "lavg15"]
        for i in range(len(args)):
            setattr(self, attrs[i], args[i])

    def get_load(self):
        return ' '.join([x for x in vars(self).values()])

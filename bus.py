# class for bus

class Bus:

    def __init__(self, _start, _end, _stops=[]):
        self.start = _start
        self.end = _end
        self.listStops = _stops

    def seekSwitchNode(self, _from, _to):
        # _from is the starting node
        # _to is the terminal node
        # return the nearest switching node
        pass

    def isDirectReachable(self, _from, _to):
        pass

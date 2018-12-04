# class for bus stops

class BusStop:

    listAllStops = []

    def __init__(self, _id, _listBus):
        self.id = _id
        self.listBus = _listBus
        self.switchStop = False
        BusStop.listAllStops.append(self)

    def addBus(self, _newBus):
        self.listBus.append(_newBus)
        self.switchStop = True

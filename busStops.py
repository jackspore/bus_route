# class for bus stops

class BusStop:

    def __init__(self, _id, _listBus):
        self.id = _id
        self.listBus = _listBus
        self.switchStop = False

    def addBus(self, _newBus):
        self.listBus.append(_newBus)
        self.switchStop = True

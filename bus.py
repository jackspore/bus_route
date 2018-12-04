# class for bus

from busStops import BusStop
import math

class Bus:

    def __init__(self, _start, _end, _stops=[]):
        self.start = _start
        self.end = _end
        self.listStops = _stops

    def getDistance(self, _from, _to):
        assert(self.isDirectReachable(_from, _to))

        idxFrom = 0
        idxTo = 0
        for idx in range(0, len(self.listStops)):
            if (self.listStops.id == _from.id):
                idxFrom = idx
            if (self.listStops.id == _to.id):
                idxTo = idx

        return math.fabs(idxTo - idxFrom)

    def seekSwitchNode(self, _from, _to):
        # _from is the starting node
        # _to is the terminal node
        # return the nearest switching node
        usableSwitch = []

        listSwitchs = self.getAllSwitchStops()
        for switch in listSwitchs:
            for bus in switch.listBus:
                if bus.isStopOnTheLine(_to) or bus.isSwitchReachable(_to):
                    usableSwitch.append(switch)

        length = len(self.listStops)
        nearSwitch = _from
        for sw in usableSwitch:
            if (self.getDistance(sw, _from) <= length):
                length = self.getDistance(sw, _from)
                nearSwitch = sw

        return nearSwitch

    def isStopOnTheLine(self, _stop):
        for stop in self.listStops:
            if (stop.id == _stop.id):
                return True

        return False

    def isDirectReachable(self, _from, _to):
        if (self.isStopOnTheLine(_from) and self.isStopOnTheLine(_to)):
            return True
        else:
            return False

    # to perform a depth first search of connect bus lines and determine if _to is
    # reachable through switch stops
    # @param _rootBus: the root search bus used to avoid endless recursive search
    def isSwitchReachable(self, _to, _rootBus):
        sw = self.getAllSwitchStops()
        for stop in sw:
            # listBus = stop.listBus
            for bus in stop.listBus:
                if bus == self or bus == _rootBus:
                    continue # avoid self and root search

                if (bus.isDirectReachable(_to)):
                    return True
                else:
                    rsw = bus.getAllSwitchStops()
                    for rstop in rsw:
                        # do a recursive search
                        if (rstop != self and rstop.isSwitchReachable(_to, _rootBus)):
                            return True
                
        return False

    def getAllSwitchStops(self):
        listSwitchs = []
        for stop in self.listStops:
            if (len(stop.listBus) > 1):
                listSwitchs.append(stop)

        return listSwitchs

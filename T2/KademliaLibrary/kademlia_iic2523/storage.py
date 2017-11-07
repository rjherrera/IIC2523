import time
from itertools import takewhile
import operator
from collections import OrderedDict

from kademlia.storage import IStorage
from multimap import MutableMultiMap

class MultipleStorage(IStorage):
    def __init__(self, ttl=604800):
        """
        By default, max age is a week.
        """
        self.data = MutableMultiMap()
        self.ttl = ttl

    def __setitem__(self, key, value):
        #  if key in self.data:
            #  del self.data[key]

        old = self.data.getall(key)

        if not isinstance(value, list):
            value = [value]

        # inneficient AF
        # Remove values that we are adding now
        new = [val for val in old if val[1] not in value]
        new.extend([(time.time(), val) for val in value])
        self.data.setall(key, new)

        self.cull()

    def cull(self):
        for k, v in self.iteritemsOlderThan(self.ttl):
            self.data.popitem(0)

    def get(self, key, default=None):
        self.cull()
        if key in self.data:
            return self[key]
        return default

    def __getitem__(self, key):
        self.cull()
        return list(map(operator.itemgetter(1), self.data.getall(key)))

    #  def __iter__(self):
        #  self.cull()
        #  return iter(self.data)

    def __repr__(self):
        self.cull()
        return repr(self.data)

    def iteritemsOlderThan(self, secondsOld):
        minBirthday = time.time() - secondsOld
        zipped = self._tripleIterable()
        matches = takewhile(lambda r: minBirthday >= r[1], zipped)
        return list(map(operator.itemgetter(0, 2), matches))

    def _tripleIterable(self):
        return [(a, b, c) for a, (b, c) in self.data.allitems()]

    def items(self):
        self.cull()
        ikeys = self.data.keys()
        ivalues = [[v[1] for v in self.data.getall(k)] for k in ikeys]
        return list(zip(ikeys, ivalues))

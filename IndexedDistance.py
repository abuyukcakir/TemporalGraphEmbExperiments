class IndexedDistance():
    def __init__(self, ind1, ind2, dist):
        self._ind1 = ind1
        self._ind2 = ind2
        self._dist = dist
        return

    def get_indices(self):
        return self._ind1, self._ind2

    def get_distance(self):
        return self._dist

    def __lt__(self, other):
      return self._dist < other._dist
    def __le__(self, other):
      return self._dist <= other._dist
    def __eq__(self, other):
      return self._dist == other._dist
    def __ne__(self, other):
      return self._dist != other._dist
    def __gt__(self, other):
      return self._dist > other._dist
    def __ge__(self, other):
      return self._dist >= other._dist

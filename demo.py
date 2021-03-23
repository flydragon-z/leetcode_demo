import copy
# from collections import Iterable
#
#
# l = [[1, 2, 3], 4]
# l_ = []
# for i in l:
#     if isinstance(i, Iterable):
#         l_.extend(i)
#     else:
#         l_.append(i)
# print(l_)
from collections import Iterable


class NestedIterator(object):
    def __init__(self, nestedList):

        while True:
            nestedList_ = []
            i = 1
            for i in nestedList:
                if isinstance(i, Iterable):
                    nestedList_.extend(i)
                    i = 0
                else:
                    nestedList_.append(i)
            nestedList = nestedList_
            if i == 1:
                self.nestedList = nestedList
                break

        self.i = 0

    def next(self) -> int:
        ret = self.nestedList[self.i]
        self.i += 1
        return ret

    def hasNext(self) -> bool:
        if self.i < len(self.nestedList):
            return True
        else:
            return False


i, v = NestedIterator([[1, 1], 2, [1, 1]]), []
while i.hasNext():
    v.append(i.next())

print(v)

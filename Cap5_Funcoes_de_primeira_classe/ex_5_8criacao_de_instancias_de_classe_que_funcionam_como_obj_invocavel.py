import random

class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()

        except IndexError:
            raise LookupError('pick fromn empty BingoCage')

    def __call__(self):
        return self.pick()


bingo = BingoCage(range(3))
print(bingo.pick())
# 1
print(bingo())
# 0
print(callable(bingo))
# True

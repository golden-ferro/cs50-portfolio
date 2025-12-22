class Jar:
        def __init__(self, capacity=12, size=0):
            if capacity < 0:
                raise ValueError
            self._capacity = capacity
            self._size = size

        def __str__(self):
            return "🍪" * self._size

        def deposit(self, n):
            self._size += n
            if self._size > self.capacity:
                raise ValueError

        def withdraw(self, n):
            self._size -= n
            if self._size < 0:
                raise ValueError

        @property
        def capacity(self):
            return self._capacity

        @property
        def size(self):
            return self._size


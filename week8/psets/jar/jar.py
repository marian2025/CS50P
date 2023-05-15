class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return f"🍪" * self.size

    def deposit(self, n):
        if self._size + n > self.capacity:
            raise ValueError("Not enough space for this many cookies")
        self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Not enough cookies in Jar")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError("Capacity setter error")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Size setter error")
        self._size = size


def main():
    jar = Jar()
    jar.deposit(1)
    print(jar)
    jar.withdraw(1)
    print(jar)
    jar.deposit(7)
    print(jar)
    jar.withdraw(2)
    print(jar)
    jar.deposit(3)
    print(jar)
    jar.withdraw(4)
    print(jar)


if __name__ == "__main__":
    main()
class MyHashMap:

    def __init__(self):
        self.t = []

    def put(self, key: int, value: int) -> None:
        if len(self.t) > 0:
            for n in self.t:
                if n[0] == key:
                    n[1] = value
                    return None
        self.t.append([key, value])
        return None

    def get(self, key: int) -> int:
        for n in self.t:
            if n[0] == key:
                return n[1]
        return -1

    def remove(self, key: int) -> None:
        for n in self.t:
            if n[0] == key:
                self.t.remove(n)
                return None
        return None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
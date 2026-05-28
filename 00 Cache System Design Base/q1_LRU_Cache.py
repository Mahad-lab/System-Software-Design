class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.recently_get = [-1 for _ in range(capacity)]
        self.data = dict()

    def get(self, key: int) -> int:
        value = self.data.get(key, None)
        if value != None:
            if key == self.recently_get[0]: 
                index = 0
            elif key in self.recently_get:
                index = self.recently_get.index(key)
            else:
                index = -1
            if index != 0:
                self.recently_get.pop(index)
                self.recently_get.insert(0, key)
        return value if value != None else -1

    def put(self, key: int, value: int) -> None:
        if key in self.data.keys():
            self.data[key] = value
        elif key not in self.data.keys() and len(self.data) < self.capacity:
            self.data[key] = value
        elif key not in self.data.keys() and len(self.data) == self.capacity:
            least_recent_key = self.recently_get[-1]
            self.data.pop(least_recent_key, None)
            self.data[key] = value

        if key not in self.recently_get:
            remove_index = -1
        else:
            remove_index = self.recently_get.index(key)

        self.recently_get.pop(remove_index or 0)
        self.recently_get.insert(0, key)

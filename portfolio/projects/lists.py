class Projects:
    def __init__(self):
        self._storage = []

    def __len__(self):
        return len(self._storage)

    # def push(self, item):
    #     self._storage.append(item)

    def pop(self, item):
        self._storage.pop(item)
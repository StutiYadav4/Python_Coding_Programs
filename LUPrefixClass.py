class LUPrefix:

    def __init__(self):
        self.array = []

    def upload(self, val):
        self.array.append(val)
        return [val]

    def longest(self):
        n = 3
        if len(self.array) == n:
            return sorted(self.array)
        else:
            return []


if __name__ == "__main__" :
    arr = LUPrefix()
    print(arr.upload(3))
    print(arr.longest())
    print(arr.upload(1))
    print(arr.longest())
    print(arr.upload(2))
    print(arr.longest())



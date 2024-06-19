class numArray:

    def __init__(self, arr):
        self.array = arr

    def printArray(self):
        return self.array
    def update(self, index, value):
        self.array[index] = value
        return self.array

    def sumRange(self, leftIndex, rightIndex):
        sum_ = 0
        for i in self.array[leftIndex:rightIndex+1]:
            sum_ += i
        return sum_


if __name__ == "__main__":
    array = numArray([1, 3, 5])
    print(array.printArray())
    print(array.sumRange(0, 2))
    print(array.update(1, 2))
    print(array.sumRange(0, 2))
import sys

class BinarySearch():
    def __init__(self):
        self.arr = []

    def binary_search(self, target):
        left = 0
        right = len(self.arr) - 1

        while (left <= right):
            mid = (right + left) // 2

            if self.arr[mid] == target:
                print("Target value at index: ", mid)
                return mid
            elif self.arr[mid] >= target:
                right = target - 1
            else:
                left = mid + 1
        
        print("Target value not present")
        
        return -1

    def process_arguments(self, args):
        for arg in args[1:]:
            self.arr.append(int(arg))


if __name__ == "__main__":
    searcher = BinarySearch()
    searcher.process_arguments(sys.argv)
    searcher.binary_search(6)
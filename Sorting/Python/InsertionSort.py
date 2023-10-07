import sys

class InsertionSort():
    def __init__(self):
        self.arr = []

    def insertion_sort(self):
        # Iterate through the array starting from the second element (index 1)
        for i in range(1, len(self.arr)):
            temp = self.arr[i]  # Store the current element in a temporary variable
            j = i - 1  # Initialize the index for the sorted part of the array
            
            # Compare the current element with the elements in the sorted part and shift them to the right
            while j >= 0 and temp < self.arr[j]:
                self.arr[j + 1] = self.arr[j]  # Shift the element to the right
                j -= 1
            
            self.arr[j + 1] = temp  # Place the current element in its correct sorted position

        print("Sorted array: ", self.arr)

    def process_arguments(self, args):
        # Parse command line arguments and convert them to integers
        for arg in args[1:]:
            self.arr.append(int(arg))

if __name__ == "__main__":
    sorter = InsertionSort()
    sorter.process_arguments(sys.argv)
    sorter.insertion_sort()  # Perform insertion sort on the input integers and print the sorted array.
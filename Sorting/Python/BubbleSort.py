import sys

class BubbleSort:
    def __init__(self):
        # Initialize an empty list to store the elements to be sorted.
        self.arr = []

    def bubble_sort(self):
        """
        Perform the bubble sort algorithm on the stored list of elements.
        """
        n = len(self.arr)  # Get the number of elements in the list.
        for i in range(n):
            for j in range(0, n - i - 1):
                # Compare adjacent elements and swap them if they are out of order.
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]


    def process_arguments(self, args):
        for arg in args[1:]:            # Extract the elements (excluding the script name).
            self.arr.append(int(arg))  

    def print_sorted_array(self):
        """
        Print the sorted array.
        """
        print("Sorted Array:", self.arr)

if __name__ == "__main__":
    # Create an instance of the BubbleSorter class.
    sorter = BubbleSort()
    
    # Process command-line arguments and store them in the class.
    sorter.process_arguments(sys.argv)
    
    # Perform the bubble sort.
    sorter.bubble_sort()
    
    # Print the sorted array.
    sorter.print_sorted_array()


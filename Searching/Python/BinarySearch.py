import sys

# Define a class named BinarySearch
class BinarySearch():
    def __init__(self):
        # Initialize an empty list to store the elements to be searched
        self.arr = []

    # Define a binary_search method to perform binary search
    def binary_search(self, target):
        left = 0  # Initialize the left pointer to the start of the list
        right = len(self.arr) - 1  # Initialize the right pointer to the end of the list

        # Perform binary search while the left pointer is less than or equal to the right pointer
        while (left <= right):
            mid = (right + left) // 2  # Calculate the middle index of the current search range

            # If the middle element is equal to the target, print the index and return it
            if self.arr[mid] == target:
                print("Target value at index: ", mid)
                return mid
            # If the middle element is greater than or equal to the target, adjust the right pointer
            elif self.arr[mid] >= target:
                right = mid - 1
            # If the middle element is less than the target, adjust the left pointer
            else:
                left = mid + 1
        
        # If the target value is not found, print a message and return -1
        print("Target value not present")
        return -1

    # Define a method to process command-line arguments and populate the array
    def process_arguments(self, args):
        for arg in args[1:]:
            self.arr.append(int(arg))

# Check if the script is being run as the main program
if __name__ == "__main__":
    searcher = BinarySearch()  # Create an instance of the BinarySearch class
    searcher.process_arguments(sys.argv)  # Process command-line arguments and populate the array
    searcher.binary_search(6)  # Perform a binary search for the target value 6

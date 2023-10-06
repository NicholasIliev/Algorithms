import sys

class LinearSearch:
    def __init__(self):
        self.arr = []  # Initialize an empty list to store elements for searching.

    def linear_search(self, q):
        j = 0

        while j < len(self.arr) and self.arr[j] != q:
            j += 1  # Increment 'j' until 'q' is found or the end of the list is reached.

        if j < len(self.arr):
            return j  # 'q' was found, return its index.
        else:
            return None  # 'q' was not found, return None.

    def process_arguments(self, args):
        """
        Process command-line arguments and extract the elements to be searched.

        Args:
            args (list): A list of command-line arguments, where the first element is the script name.

        Returns:
            None
        """
        for arg in args[1:]:
            self.arr.append(int(arg))  # Convert and add each argument to the 'arr' list.

if __name__ == "__main__":
    searcher = LinearSearch()  # Create an instance of the LinearSearch class.
    searcher.process_arguments(sys.argv)  # Process command-line arguments.
    result = searcher.linear_search(6)  # Perform a linear search for the value 6.
    if result is not None:
        print(f"Found at index {result}")  # Print the index where 6 was found.
    else:
        print("Not found")  # Print a message indicating that 6 was not found.

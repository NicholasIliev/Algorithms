import math

def find_n_satisfying_inequality():
    n = 1   # Start with an initial initial estimate for n

    while True:
        lg2n = math.log2(n)  # Calculate lg2n
        if n > 32 * lg2n:
            return n  # Found the value of n that satisfies the inequality
        n += 1  # Increment n for the next iteration

result = find_n_satisfying_inequality()
print("The value of n that satisfies the inequality is approximately:", result)

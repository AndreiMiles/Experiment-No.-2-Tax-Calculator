import time

def sum_using_for_loop(n):
    start_time = time.time()
    total_sum = 0
    for i in range(1, n+1):
        total_sum += i
    end_time = time.time()
    execution_time = end_time - start_time
    return total_sum, execution_time

# Test the function with different values of n
n_values = [10, 100, 1000, 10000, 100000]
for n in n_values:
    total_sum, execution_time = sum_using_for_loop(n)
    print(f"Sum of numbers from 1 to {n}: {total_sum}")
    print(f"Execution time: {execution_time} seconds")

import time

def sum_using_while_loop(n):
    start_time = time.time()
    sum = 0
    i = 1
    while i <= n:
        sum += i
        i += 1
    end_time = time.time()
    execution_time = end_time - start_time
    return sum, execution_time

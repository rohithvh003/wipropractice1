import math
import time
from multiprocessing import Pool, cpu_count


numbers = [5000, 6000, 5500, 4500, 7000]


def compute_factorial(n):
    return math.factorial(n)


if __name__ == "__main__":

    # Sequential
    starttime1 = time.time()
    seq_result = []

    for num in numbers:
        result = compute_factorial(num)
        seq_result.append(result)
        print(f"Sequential: Factorial {num} calculated")

    seqtime = time.time() - starttime1
    print(f"\nSequential time: {seqtime}")

    # Parallel
    starttime2 = time.time()

    with Pool(cpu_count()) as pool:
        parallel_result = pool.map(compute_factorial, numbers)

    for num in numbers:
        print(f"Multiprocessing: Factorial {num} calculated")

    parallel_time = time.time() - starttime2
    print(f"\nParallel time: {parallel_time}")

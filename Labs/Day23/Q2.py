import math
import time
from multiprocessing import Pool, cpu_count

numbers = [5000, 6000, 5500, 4500, 7000]

def compute_factorial(n):
    return math.factorial(n)

def factorial_digits(n):
    return int(sum(math.log10(i) for i in range(1, n + 1))) + 1


if __name__ == "__main__":
    starttime1 = time.time()
    seq_digits = []

    for num in numbers:
        compute_factorial(num)
        seq_digits.append(factorial_digits(num))

    seqtime = time.time() - starttime1

    print("Sequential Results:")
    for num, digits in zip(numbers, seq_digits):
        print(f"Factorial of {num} has {digits} digits")

    print(f"\nSequential time: {seqtime}")

    starttime2 = time.time()

    with Pool(cpu_count()) as pool:
        parallel_digits = pool.map(factorial_digits, numbers)

    parallel_time = time.time() - starttime2

    print("\nMultiprocessing Results:")
    for num, digits in zip(numbers, parallel_digits):
        print(f"Factorial of {num} has {digits} digits")

    print(f"\nParallel time: {parallel_time}")


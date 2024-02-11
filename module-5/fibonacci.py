#!/usr/local/bin/python3
import sys

def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        if n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 fibonacci.py <number>")
        sys.exit(1)

    fib_number = int(sys.argv[1])
    fib = caching_fibonacci()
    print(fib(fib_number))


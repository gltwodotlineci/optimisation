import time

n = 31


def fib(n: int) -> int:
    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)

t = time.time()
fib_nbr = fib(n)
print(fib_nbr)
print(f"Time execution is: ", time.time() - t)

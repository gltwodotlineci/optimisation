
mem = {}
def fib_mem(n: int, mem: dict) -> int:
    if n in mem:
        return mem[n]
    
    if n < 2:
        mem[n] = n
        return n
    
    mem[n] = fib_mem(n-1, mem) + fib_mem(n-2, mem)
    return mem[n]

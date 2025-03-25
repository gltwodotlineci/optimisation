import click, time
from brutforce import fib
from memoization import fib_mem

@click.group()
def cli():
    pass


@cli.command()
@click.argument('n')
def execute_fibonacci(n):
    t = time.time()
    fib_nbr = fib(int(n))
    print(f"The fibonacci sequence of {n} is: {fib_nbr}")
    print(f"The time for this execution is: {time.time() - t} seconds")


@cli.command()
@click.argument('n')
def call_fib_mem(n: int):
    t = time.time()
    mem = {}
    fib_nb = fib_mem(int(n), mem)
    print(f"The fibonacci sequence of {n} is: {fib_nb}")
    print(f"The time for this execution is: {time.time() - t} seconds")

if __name__ == '__main__':
    cli()

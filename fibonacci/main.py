import click, time
from brutforce import fib

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


if __name__ == '__main__':
    cli()

import click, time
from brutforce import brute_force
from lists_dt import json_lists
from optimisation import optimize_solution


all_lists = json_lists()


@click.group()
def cli():
    pass


@cli.command()
@click.argument('list_name')
def call_brutforce(list_name: str) -> None:
    choosed_list = all_lists.get(list_name)
    sub_kadans = brute_force(choosed_list)
    print("The list you choosed has kadan's sublist of: ")
    print(sub_kadans)
    print(" ")
    if  isinstance(sub_kadans, int):
        print(f"And its some is: ", (sub_kadans))
    else:
        print(f"And its some is: ", sum(sub_kadans))


@cli.command()
@click.argument('list_name')
def call_optimization(list_name: str) -> None:
    choosed_list = all_lists.get(list_name)
    sub_kadans = optimize_solution(choosed_list)
    print("The list you choosed has kadan's sublist of: ")
    print(sub_kadans)
    print(" ")
    print(f"And its some is: ", sum(sub_kadans))



if __name__ == '__main__':
    cli()

import click, time
from brutforce import brute_force                                             


all_lists = {
    "lst1": [1, 3, 5, -4, 2, 1],
    "negativ_lst": [-1, -3, -5, -2, -6],
    "lg_lst": [4, -1, 2, 1, -7, 5, 3, -2, 6, -10, 4, 2, -1, 2, -3]
}

@click.group()
def cli():
    pass


@cli.command()
@click.argument('list_name')
def call_brutforce(list_name: str) -> None:
    choosed_list = all_lists.get(list_name)
    sub_kadans = brute_force(choosed_list)
    print("The list you choosed is")
    print(choosed_list)
    print(" ")
    print("And its kadan's sublist is: ")
    print(sub_kadans)


if __name__ == '__main__':
    cli()

import time, click
from brutforce import get_wallet
from refacto_fc import create_actions_list
url1 = "data/list_actions.csv"
url2 = "data/list_actions2.csv"

actions1 = create_actions_list(url1, missing_profit=True)
actions2 = create_actions_list(url2, missing_profit=False)

all_actions = {'actions1': actions1, 'actions2': None}

# Creaing a click regroupment decorator for all the methods
@click.group()
def cli():
    pass


@cli.command()
@click.argument('action')
@click.argument('budget')
def launching_brutforce(action: str, budget:float):
    actions = all_actions.get(action)
    t1 = time.time()
    wallet, profit = get_wallet(actions, float(budget))
    print(f"The max profit is {profit} from the wallet: {wallet}")
    print("Time execution -> ", time.time() - t1)


def launch_optimized()

if __name__ == "__main__":
    cli()

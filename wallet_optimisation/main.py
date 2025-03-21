import time, click
from brutforce import get_wallet
from refacto_fc import create_actions_list
from optimisation import prepare_actions, find_wallet
from optimisation import dynamic_knapsack

url1 = "data/list_actions.csv"
url2 = "data/list_actions2.csv"

actions1 = create_actions_list(url1, missing_profit=True)
actions2 = create_actions_list(url2, missing_profit=False)

all_actions = {'actions1': actions1, 'actions2': actions2}

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

@cli.command()
@click.argument('action')
@click.argument('budget')
def launch_optimized(action: str, budget: int):
    t1 = time.time()
    n = int(budget)
    if action == "actions1":
        big_dt = False
    elif action == "actions2":
        big_dt = True
    print("nnnn -> ", n)
    actions = all_actions.get(action)
    actions_nb = len(actions) + 1
    action_data = prepare_actions(actions)
    knapsack_tab, names = dynamic_knapsack(action_data, actions_nb, big_dt)
    wallet = find_wallet(knapsack_tab, names, actions_nb)
    best_profit = round(knapsack_tab[actions_nb-1][n],2)
    print("<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(f"The wallet with the best profit is: {list(wallet.values())}")
    wallet_val = sum([x[1] for x in list(wallet.values())])
    print(f"The wallet price is: {wallet_val} euros")
    print("   ")
    print(f"And it's profit is: {best_profit}")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Time execution -> ", time.time() - t1)


if __name__ == "__main__":
    cli()

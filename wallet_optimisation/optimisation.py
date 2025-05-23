from refacto_fc import create_actions_list
import time
from collections import deque

url = "data/list_actions.csv"
actions = create_actions_list(url, missing_profit= True)


def prepare_actions(actions: list) -> list:
    prepared_dt = deque(actions)
    prepared_dt.appendleft([None, None, None, None])
    return list(prepared_dt)


actions_final_lst = prepare_actions(actions)
actions_nb = len(actions_final_lst)


def dynamic_knapsack(actions: list, n: int, big_dt: bool) -> tuple[list, list]:
    # Creating the first row of the table
    tabulation_dyn = [[0.0] * 501 for _ in range(n)]
    # initializint action names table
    action_names = []
    # Filling the table
    if big_dt:
        c2 = 2
    else:
        c2 = 3
    for i in range(0, n):
        row = []
        action = []
        for j in range(0,501):
            if i == 0:
                row.append(0.0)
            else:
                action.append(actions[i])
                value_action = actions[i][1]
                profit = actions[i][c2]

                if value_action <= j:
                    profit_ante = tabulation_dyn[i-1][j]
                    max_profit = max(profit_ante, profit + tabulation_dyn[i-1][j-value_action])
                    row.append(max_profit)
                else:
                    row.append(tabulation_dyn[i-1][j])
        
        action_names.append(action)
        tabulation_dyn[i] = row

    return tabulation_dyn, action_names


# searching for the wallet that created the bes profit
def find_wallet(knapsack_tab: list, action_names_lst: list, n: int)-> dict:
    wallet = {}
    ind_r = n - 1
    ind_c = 500
    while ind_r > 0 and ind_c > 0:
        # Geting the wallet actions
        if knapsack_tab[ind_r][ind_c] != knapsack_tab[ind_r-1][ind_c]:  
            action = action_names_lst[ind_r][0]
            wallet[ind_r] = action
            ind_c -= action[1]

        ind_r -= 1

    return wallet

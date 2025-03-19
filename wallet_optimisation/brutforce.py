from itertools import combinations


# Geting the highest profit
def get_profit(actions: list[tuple], budget: float) -> float | None:
    profit = 0.0
    action_value = 0.0
    for action in actions:
        action_value += action[1]
        profit += action[3]
        if action_value > budget:
            return None

    return profit


# Creating a wallet with the bes action combinations
def get_wallet(actions: list, budget: float) -> tuple[list, float]:
    best_combination = None
    max_profit = 0
    for i in range(1, len(actions) + 1):
        for combination in combinations(actions, i):
            profit_combination = get_profit(combination, budget)
            if profit_combination is None:
                continue
            if max_profit < profit_combination :
                max_profit = profit_combination
                best_combination = combination

    return best_combination, max_profit

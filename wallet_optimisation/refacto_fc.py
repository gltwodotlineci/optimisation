import csv

def calcul_profit(action: list) -> float:
    percent = float(action[2][:-1])/100
    price = action[1]
    return price * percent

# parsing csv data into list
def create_actions_list(path:str, missing_profit: bool=True)-> list:
    actions = []
    with open(path, 'r') as file:
        actions_dt = csv.reader(file)
        next(actions_dt)
        for action in actions_dt:
            # changing action price in integer
            if missing_profit is True:
                action[1] = int(action[1])
                calculated_profit = round(calcul_profit(action), 2)
                action.append(calculated_profit)
            else:
                intermed_price = float(action[1]) * 10
                action[1] = int(intermed_price)
                if action[1] <= 0:
                    continue
                action[2] = float(action[2])

            actions.append(action)

        return actions

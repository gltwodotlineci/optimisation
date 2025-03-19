from refacto_fc import create_actions_list
import time

url = "data/list_actions.csv"
actions = create_actions_list(url, missing_profit= True)

actions_nb = len(actions)
total_n = (2**actions_nb-1)
print(total_n)

import time
from refacto_fc import create_actions_list
from itertools import combinations

url = "data/list_actions.csv"
profit_action_list = create_actions_list(url, missing_profit=True)

# Geting the highest profit

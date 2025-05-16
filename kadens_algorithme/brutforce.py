
def brute_force(lst: list[int]) -> int | None:
    """
    Find the maximum number in a list using brute force.
    """
    if check_negative(lst):
        return max(lst)

    max_list = []
    for i in range(len(lst)):
        for j in range(1,len(lst)):
            if lst[i:j] == []:
                continue

            if sum(max_list) < sum(lst[i:j]):
                max_list = lst[i:j]

    if sum(max_list) < sum(lst):
        return lst
    return max_list


def check_negative(lst: list[int]) -> bool:
    """
    Check if the list contains only negative numbers.
    """
    count_neg = 0
    for i in lst:
        if i < 0:
            count_neg += 1

    return count_neg == len(lst)


def compare_lists(lst1: list[int], lst2: list[int]) -> bool:
    if sum(lst1) < sum(lst2):
        return True
    return False

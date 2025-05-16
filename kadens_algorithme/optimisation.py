lst1 = [1, 3, 5, -4, 2, 1]
negativ_lst = [-1, -3, -5, -2, -6]
lg_lst = [4, -1, 2, 1, -7, 5, 3, -2, 6, -10, 4, 2, -1, 2, -3]
very_lg_list = [
    -5, 3, -2, 9, -1, 2, -8, 10, 15, -3,
    -4, 7, -10, 12, -7, 5, -2, 6, -11, 4,
    -1, 8, -9, 3, -6, 2, 1, -3, 9, -2,
    4, -8, 10, -3, 6, -2, -5, 7, -4, 3,
    -1, 2, -6, 5, 8, -7, 4, -2, 3, -5
]


def optimize_solution(given_lst: list[int]) -> list[int] | int:
    if not given_lst:
        return 0  # or raise an exception, depending on desired behavior

    max_sum = current_sum = given_lst[0]
    max_l = max_r = temp_l = 0

    for right in range(1, len(given_lst)):
        if current_sum < 0:
            current_sum = given_lst[right]
            temp_l = right
        else:
            current_sum += given_lst[right]

        if current_sum > max_sum:
            max_sum = current_sum
            max_l = temp_l
            max_r = right

    return given_lst[max_l:max_r+1]

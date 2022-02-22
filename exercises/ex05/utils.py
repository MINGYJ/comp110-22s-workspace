"""The utils functions contains many functions used by test program."""


__author__ = "730486611"


def only_evens(number_list: list[int]) -> list[int]:
    count: int = 0
    even_list: list[int] = list()
    for count in number_list:
        if(count % 2 == 0):
            even_list.append(count)
    return even_list


def sub(n_list: list[int], start: int, end: int) -> list[int]:
    count: int = 0
    sub_list: list[int] = list()
    if(start < 0):
        start = 0
    if(end > len(n_list)):
        end = len(n_list)
    for number in n_list:
        if(count >= start and count < end):
            sub_list.append(number)
        count += 1
    return sub_list
            

def concat(a_list: list[int], b_list: list[int]) -> list[int]:
    ab_list: list[int] = a_list
    for numbers in b_list:
        ab_list.append(numbers)
    return ab_list
"""The program use dictionary to creat functions."""
__author__ = "730486611"


def invert(old_dict: dict[str, str]) -> dict[str, str]:
    """Inverse the keyword and valur of a dictionary."""
    inverse_dict: dict[str, str] = dict()
    for key in old_dict:
        for inverse_key in inverse_dict:
            if inverse_key == old_dict[key]:
                raise KeyError
        inverse_dict[old_dict[key]] = key
    return inverse_dict


def favorite_color(color_dict: dict[str, str]) -> str:
    """Find the most frequent color."""
    max_number: int = 0
    max_color: str = ""
    color_list: list[str] = list()
    for key in color_dict:
        color_list.append(color_dict[key])
    counted_color: dict[str, int] = count(color_list)
    for key in counted_color:
        if counted_color[key] > max_number:
            max_number = counted_color[key]
            max_color = key
    return max_color


def count(count_list: list[str]) -> dict[str, int]:
    """Count the frequency of elements in a list."""
    count_dict: dict[str, int] = dict()
    i: int = 0
    while i < len(count_list):
        flag: bool = False
        for key in count_dict:
            if count_list[i] == key:
                flag = True
                count_dict[key] += 1
        if not flag:
            count_dict[count_list[i]] = 1
        i += 1
    return count_dict
                

        
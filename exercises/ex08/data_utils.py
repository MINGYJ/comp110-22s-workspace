"""Dictionary related utility functions."""

__author__ = ""

# Define your functions below


from csv import DictReader


def read_csv_rows(route: str) -> list[dict[str, str]]:
    """Open the csv and save it into a list."""
    final_list: list[dict[str, str]] = []
    csv_file = open(route, "r", encoding="utf8")
    csv_reader = DictReader(csv_file)
    for rows in csv_reader:
        final_list.append(rows)
    csv_file.close()
    return final_list


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Store all values in a column list[str]."""
    result_list: list[str] = []
    for row in table:
        item: str = row[column]
        result_list.append(item)
    return result_list


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transfer a row table to a column table."""
    result_dict: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result_dict[column] = column_values(row_table, column)
    return result_dict


def head(table: dict[str, list[str]], row: int) -> dict[str, list[str]]:
    """Return the first several rows in table."""
    result_dict: dict[str, list[str]] = {}
    for column in table:
        count: int = 0
        result_dict[column] = []
        if row > len(table[column]):
            row = len(table[column])
        while count < row:
            result_dict[column].append(table[column][count])
            count += 1
    return result_dict


def select(table: dict[str, list[str]], key_list: list[str]) -> dict[str, list[str]]:
    """Select some of the column keys and return them in a new dictionary."""
    result_dict: dict[str, list[str]] = {}
    for column in table:
        if column in key_list:
            result_dict[column] = table[column]
    return result_dict


def concat(a_dict: dict[str, list[str]], b_dict: dict[str, list[str]]) -> dict[str, list[str]]:
    """Add two dictionary together."""
    result_dict: dict[str, list[str]] = a_dict
    for column in b_dict:
        if column in result_dict:
            result_dict[column] = result_dict[column] + b_dict[column]
        else:
            result_dict[column] = b_dict[column]
    return result_dict


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

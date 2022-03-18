"""Dictionary related utility functions."""

__author__ = ""

# Define your functions below


from csv import DictReader
from typing import final


def read_csv_rows(route: str) -> list[dict[str, str]]:
    """Open the csv and save it into a list."""
    final_list: list[dict[str, str]] = []
    csv_file = open(route, "r", encoding="utf8")
    csv_reader = DictReader(csv_file)
    for rows in csv_reader:
        final_list.append(rows)
    csv_file.close()
    return final_list


def column_values(table: )
"""Utility functions."""

__author__ = "730484862"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all vlaues in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row: 
        result[column] = column_values(row_table, column)

    return result


def head(table: dict[str, list[str]], num_of_rows: int) -> dict[str, list[str]]:
    """Produce a new column based table with N rows of data per column."""
    result: dict[str, list[str]] = {}
    for column in table:
        holding_list: list[str] = []
        i: int = 0
        while i < num_of_rows and i < len(table[column]):
            holding_list.append(table[column][i])
            i += 1
        result[column] = holding_list
    return result


def select(table: dict[str, list[str]], copy_list: list[str]) -> dict[str, list[str]]:
    """Produce a new column based table with only a some of the origninal columns."""
    result: dict[str, list[str]] = {}
    for item in copy_list:
        result[item] = table[item]
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column based table with data from two tables combined."""
    result: dict[str, list[str]] = {}
    for column in table1:
        result[column] = table1[column]
    for column2 in table2:
        if column2 in result:
            result[column2] = result[column2] + table2[column2]
        else:
            result[column2] = table2[column2]
    return result


def count(frequency_list: list[str]) -> dict[str, int]:
    """A function that counts the frequency of an value in a list."""
    result: dict[str, int] = {}
    for item in frequency_list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result

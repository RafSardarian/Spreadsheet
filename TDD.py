"""Test-Driven Development"""
from spreadsheet import SpreadSheet
from cell import Cell
from datetime import date

test = SpreadSheet(5, 6)


def for_all_cases(function, value):
    if function == value:
        print(f'{function} function passed')
    else:
        print(f'{function} function failed')


# Tests for Cell
def test_set_get_value(value: str):
    cell = Cell(value)
    for_all_cases(cell.get_value(), value)


def test_set_get_color(color):
    cell = Cell('hello')
    cell.set_color(color)
    for_all_cases(cell.get_color(), color)


def test_to_int(value):
    cell = Cell(value)
    for_all_cases(type(cell.to_int(), int))


def test_to_float(value):
    cell = Cell(value)
    cell.to_float()
    for_all_cases(cell.to_float(), float)


def test_to_date(value):
    cell = Cell(value)
    cell.to_date()
    for_all_cases(type(cell.get_value()), date)


def test_reset(value):
    cell = Cell(value)
    cell.reset()
    for_all_cases(cell.get_value(), '')

# Tests for Spreadsheet


def test_make_sheet(row: int, column: int):
    sheet = SpreadSheet(row,column)
    for_all_cases(shape(sheet.get_cells()), (row, column))


def shape(array: list):
    row = len(array)
    column = len(array[0])
    return row, column


def test_set_cell_at(row: int, column: int, value: str):
    sheet = SpreadSheet(row + 1, column + 1)
    sheet.set_cell_at(row, column, value)
    for_all_cases(sheet.get_cells()[row][column].get_value(), value)


def test_get_cell_at(row: int, column: int):
    sheet = SpreadSheet(row + 4, column + 4)
    for_all_cases(sheet.get_cell_at(row, column), sheet.get_cells()[row][column].get_value())


def test_add_row():
    pass


def test_remove_row():
    pass


def test_add_column():
    pass


def test_remove_column():
    pass


def test_swap_rows():
    pass


def test_swap_columns():
    pass



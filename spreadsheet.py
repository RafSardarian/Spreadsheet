from cell import Cell


class SpreadSheet:
    def __init__(self, row: int, column: int) -> None:
        self.__cells = []
        self.__make_sheet(row, column)

    def get_cells(self):
        return self.__cells

    def __make_sheet(self, row: int, column: int) -> None:
        for i in range(row):
            self.__cells.append(['']*column)

    def set_cell_at(self, row: int, column: int, value: str) -> None:
        self.__cells[row][column] = Cell(value)

    def get_cell_at(self, row: int, column: int) -> Cell:
        return self.__cells[row][column]

    def add_row(self, position_row) -> None:
        self.__cells.insert(position_row, [''] * len(self.__cells[0]))

    def remove_row(self, position_row) -> None:
        self.__cells.pop(position_row - 1)

    def add_column(self, position_column) -> None:
        for row in self.__cells:
            row.insert(position_column, [''])

    def remove_column(self, position_column) -> None:
        for row in self.__cells:
            row.pop(position_column - 1)

    def swap_row(self, row1, row2) -> None:
        self.__cells[row1 - 1], self.__cells[row2 - 1] = self.__cells[row2 - 1], self.__cells[row1 - 1]

    def swap_column(self, column1, column2) -> None:
        for row in self.__cells:
            self.__cells[row][column1 - 1], self.__cells[row][column2 - 1] = \
                self.__cells[row][column2 - 1], self.__cells[row][column1 - 1]





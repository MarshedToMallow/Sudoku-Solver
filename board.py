import numpy as np

class Houses:
    def __init__(self, table):
        self.rows = table
        self.columns = np.transpose(table)
        self.blocks = np.array(np.dsplit(np.array(np.vsplit(table, 3)), 3)).reshape(9, 9)

class HouseSets:
    def __init__(self, houses):
        self.rows = [set(row) for row in houses.rows]
        self.columns = [set(column) for column in houses.columns]
        self.blocks = [set(blocks) for blocks in houses.blocks]
    
    def update(self, row, col, value):
        pass

class Board:
    def __init__(self, table):
        self.houses = Houses(table)
        self.house_sets = HouseSets(self.houses)

    def search(self):
        pass

    def _get_next_cell(self):
        pass

    def _get_blocks(self, cell):
        pass

# Instead of determining the exact set of possible states per cell,
# maintain a count for each row and column as to how many remaining values there are.
# Take the lowest count for row and column (excluding 0) to select the next cell to try.
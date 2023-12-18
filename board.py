import numpy as np
import copy

class Houses:
    def __init__(self, table):
        self.rows = table
        self.columns = np.transpose(table)
        self.blocks = np.array(np.dsplit(np.array(np.vsplit(table, 3)), 3)).reshape(9, 9)

class HouseSets:
    def __init__(self, houses):
        values = set(range(1, 10))
        self.rows = [values - set(row) for row in houses.rows]
        self.columns = [values - set(column) for column in houses.columns]
        self.blocks = [values - set(block) for block in houses.blocks]

    def update(self, row, col, value):
        self.rows[row] - {value}
        self.columns[col] - {value}
        
        block_row = row // 3
        block_col = col // 3

        self.blocks[block_row + 3 * block_col] - {value}

    def get_set(self, row, col):
        result = self.rows[row]
        result = result.intersection(self.columns[col])

        block_row = row // 3
        block_col = col // 3

        block = self.blocks[block_row + 3 * block_col]

        result = result.intersection(block)
        return result

class Counts:
    def __init__(self, housesets):
        self.rows =  [len(row) for row in housesets.rows]
        self.columns = [len(column) for column in housesets.columns]
    
    def update(self, row, col):
        self.rows[row] -= 1
        self.columns[col] -= 1
    
    def select(self):
        row = min(range(9), key = lambda x: (self.rows[x] - 1) % 10)
        col = min(range(9), key = lambda x: (self.columns[x] - 1) % 10)
        return (row, col)

class Board:
    def __init__(self, table):
        self.table = table
        self.house_sets = HouseSets(Houses(table))
        self.counts = Counts(self.house_sets)

    def search(self, depth = 0):
        #print(depth)
        row, col = self.counts.select()

        values = self.house_sets.get_set(row, col)
        if len(values) == 0:
            if self.solved():
                return self
            return None

        for value in values:
            new = copy.deepcopy(self)
            new.update(row, col, value)
            outcome = new.search(depth = depth + 1)

            if not(outcome is None):return outcome
        return None

    def update(self, row, col, value):
        self.table[row][col] = value
        self.house_sets.update(row, col, value)
        self.counts.update(row, col)
    
    def solved(self):
        for row in self.house_sets.rows:
            if len(row) != 0:return False
        
        for column in self.house_sets.columns:
            if len(column) != 0:return False
        
        for block in self.house_sets.blocks:
            if len(block) != 0:return False
        
        return True

# Instead of determining the exact set of possible states per cell,
# maintain a count for each row and column as to how many remaining values there are.
# Take the lowest count for row and column (excluding 0) to select the next cell to try.

if __name__ == "__main__":
    table = np.array([[9, 1, 0, 0, 0, 0, 4, 2, 7],
              [0, 0, 0, 0, 0, 3, 9, 1, 5],
              [2, 5, 4, 7, 0, 0, 6, 8, 0],
              [4, 7, 0, 0, 8, 6, 0, 3, 2],
              [0, 6, 0, 4, 0, 0, 0, 0, 8],
              [5, 0, 0, 0, 1, 2, 0, 6, 0],
              [3, 4, 0, 6, 2, 0, 0, 0, 1],
              [0, 0, 0, 3, 0, 0, 0, 0, 0],
              [0, 2, 6, 0, 0, 8, 0, 0, 9]])
    board = Board(table)
    solution = board.search()
    print(solution.table)
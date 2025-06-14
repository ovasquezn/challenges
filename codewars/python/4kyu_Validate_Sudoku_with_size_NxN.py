class Sudoku(object):
    def __init__(self, data):
        self.data = data
        self.size = len(data)
        self.subgrid_size = int(self.size ** 0.5)
    def is_valid(self):
        partitions = self._get_partitions()
        for partition in partitions:
            if not self._is_valid_partition(partition):
                return False
        return True
    def _get_partitions(self):
        partitions = []
        # Rows
        for row in self.data:
            partitions.append(row)
        # Columns
        for col in range(self.size):
            partitions.append([self.data[row][col] for row in range(self.size)])
        # Subgrids
        for row in range(0, self.size, self.subgrid_size):
            for col in range(0, self.size, self.subgrid_size):
                subgrid = []
                for r in range(row, row + self.subgrid_size):
                    for c in range(col, col + self.subgrid_size):
                        subgrid.append(self.data[r][c])
                partitions.append(subgrid)
        return partitions
    def _is_valid_partition(self, partition):
        seen = set()
        for num in partition:
            if num != 0:
                if num in seen or num < 1 or num > self.size:
                    return False
                seen.add(num)
        return True
# Example usage     

sudoku = Sudoku([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 2, 8, 0],
    [0, 0, 4, 1, 9, 5, 7],
    [2]
])
print(sudoku.is_valid())  # Output: False (incomplete sudoku)
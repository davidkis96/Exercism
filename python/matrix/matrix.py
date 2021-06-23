class Matrix:
    def __init__(self, matrix_string):
        self.matrix = []
        rows = matrix_string.split("\n")
        for line in rows:
            row = [int(num) for num in line.split()]
            self.matrix.append(row)

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [num[index - 1] for num in self.matrix]

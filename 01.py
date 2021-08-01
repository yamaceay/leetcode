import copy
class Solution(object):
    class UnionFind:
        def __init__(self, uf=None):
            self.components = []
            if uf is not None:
                self.components = uf.result()
        def union_one(self, x):
            x_place = self.find(x)
            if x_place == -1:
                self.components.append([x])
        def union(self, x, y):
            x_place = self.find(x)
            y_place = self.find(y)
            if x_place == -1 and y_place == -1:
                self.components.append([x, y])
            elif x_place == y_place:
                return
            elif x_place == -1:
                self.components[y_place].append(x)
            elif y_place == -1:
                self.components[x_place].append(y)
            else:
                self.components[x_place].extend(self.components[y_place])
                del self.components[y_place]
        def find(self, x):
            for i in range(len(self.components)):
                if x in self.components[i]:
                    return i
            return -1
        def result(self):
            return self.components
          
    def hashCode(self, row, col):
        return "-".join([str(row), str(col)])
    def reverseHashCode(self, string):
        return [int(x) for x in string.split("-")]
    def findValues(self, grid, value):
        values = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == value:
                    values.append({"row": i, "col": j})
        return values
    def findHashCodes(self, grid, value):
        values = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == value:
                    values.append(self.hashCode(i, j))
        return values
    def findSolutionRecursive(self, uf, grid, ones, one):
        ones.remove(one)
        row, col = self.reverseHashCode(one)
        for new_row, new_col in zip([row-1, row, row+1, row], [col, col-1, col, col+1]):
            if new_row not in range(len(grid)) or new_col not in range(len(grid[0])):
                continue
            new_one = self.hashCode(new_row, new_col)
            if new_one in ones:
                uf.union(one, new_one)
                self.findSolutionRecursive(uf, grid, ones, new_one)
    def findSolution(self, grid):
        uf = self.UnionFind()
        ones = self.findHashCodes(grid, 1)
        while len(ones):
            one = ones[0]
            uf.union_one(one)
            self.findSolutionRecursive(uf, grid, ones, one)
        return uf
    def findMax(self, uf):
        maxSize = 0
        for component in uf.result():
            maxSize = max(maxSize, len(component))
        return maxSize
    def largestIsland(self, grid):
        zeros = self.findHashCodes(grid, 0)    
        uf = self.findSolution(grid)
        maxSize = max(1, self.findMax(uf))
        for zero in zeros:
            uf_new = copy.deepcopy(uf)
            row, col = self.reverseHashCode(zero)
            for new_row, new_col in zip([row-1, row, row+1, row], [col, col-1, col, col+1]):
                if new_row in range(len(grid)) and new_col in range(len(grid[0])) and grid[new_row][new_col]:
                    uf_new.union(zero, self.hashCode(new_row, new_col))
                    new_set = uf_new.find(zero)
                    maxSize = max(len(uf_new.result()[new_set]), maxSize)
        return maxSize
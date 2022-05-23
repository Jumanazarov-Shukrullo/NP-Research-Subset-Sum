class SubsetSum:

    def __init__(self, array_size, target_sum):
        self.array_size = array_size
        self.array_elements = []
        self.target_sum = target_sum
        self.dp_table = [[-1 for _ in range(target_sum + 1)] for _ in range(array_size + 1)]


class BruteForce(SubsetSum):
    def recursive_function(self, arr, size, target_sum):
        if target_sum == 0:
            return True
        if size < 0 or target_sum < 0:
            return False
        include = self.recursive_function(arr, size - 1, target_sum - arr[size])
        exclude = self.recursive_function(arr, size - 1, target_sum)
        return include or exclude


class Memoization:

    def __init__(self, array_size, target_sum):
        self.array_size = array_size
        self.target_sum = target_sum
        self.table = [[-1 for _ in range(4000)] for _ in range(4000)]

    def solve(self, array, array_size, target_sum):
        table = self.table
        if target_sum == 0:
            return 1
        if array_size <= 0:
            return 0
        if table[array_size - 1][target_sum] != -1:
            return table[array_size - 1][target_sum]
        if array[array_size - 1] > target_sum:
            table[array_size - 1][target_sum] = self.solve(array, array_size - 1, target_sum)
            return table[array_size - 1][target_sum]
        else:
            table[array_size - 1][target_sum] = self.solve(array, array_size - 1, target_sum)
            return table[array_size - 1][target_sum] or self.solve(array, array_size - 1, target_sum - array[array_size - 1])


class DynamicProgramming(SubsetSum):

    def solve(self, array, size, target_sum):
        self.array_elements = array
        self.array_size = size
        self.target_sum = target_sum
        for i in range(size):
            for j in range(target_sum):
                if i == 0:
                    array[i][j] = False
                if j == 0:
                    array[i][j] = True
        # we have to construct the table with the cells one by one
        for rowIndex in range(1, size + 1):
            for colIndex in range(1, target_sum + 1):
                if array[rowIndex - 1] > colIndex:
                    array[rowIndex][colIndex] = array[rowIndex - 1][colIndex]
                else:
                    array[rowIndex][colIndex] = array[rowIndex-1][colIndex] or array[rowIndex - 1][colIndex - array[rowIndex - 1]]
        return self.dp_table[size][target_sum]

    def show_result(self):
        print("The problem is achievable: %s " % self.dp_table[len(self.array_elements)][self.target_sum])

        if not self.dp_table[len(self.array_elements)][self.target_sum]:
            return

        # print out the items in the subset
        col_index = self.target_sum
        row_index = len(self.array_elements)

        while col_index > 0 or row_index > 0:
            if self.dp_table[row_index][col_index] == self.dp_table[row_index - 1][col_index]:
                row_index = row_index - 1
            else:
                print("We take: %d" % self.array_elements[row_index - 1])
                col_index = col_index - self.array_elements[row_index - 1]
                row_index = row_index - 1
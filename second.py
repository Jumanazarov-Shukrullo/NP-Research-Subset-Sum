# 27.03.2022
# approach by dynamic programming in pseudo-polynomial time complexity

class SubsetSum:

    def __init__(self, nums, target_sum):
        self.nums = nums
        self.target_sum = target_sum
        self.array = [[False for _ in range(target_sum + 1)] for _ in range(len(nums) + 1)]

    def solve(self):

        # initialize the first row and first column
        for i in range(len(self.nums) + 1):
            self.array[i][0] = True

        # we have to construct the table with the cells one by one
        for rowIndex in range(1, len(self.nums) + 1):
            for colIndex in range(1, self.target_sum + 1):
                if colIndex < self.nums[rowIndex - 1]:
                    self.array[rowIndex][colIndex] = self.array[rowIndex - 1][colIndex]
                else:
                    if self.array[rowIndex - 1][colIndex]:
                        # this is when we do NOT include the given item rowIndex
                        self.array[rowIndex][colIndex] = self.array[rowIndex - 1][colIndex]
                    else:
                        # do include the item i
                        self.array[rowIndex][colIndex] = self.array[rowIndex - 1][colIndex - self.nums[rowIndex - 1]]

    def show_result(self):
        print("The problem is achievable: %s " % self.array[len(self.nums)][self.target_sum])

        if not self.array[len(self.nums)][self.target_sum]:
            return

        # print out the items in the subset
        col_index = self.target_sum
        row_index = len(self.nums)

        while col_index > 0 or row_index > 0:
            if self.array[row_index][col_index] == self.array[row_index - 1][col_index]:
                row_index = row_index - 1
            else:
                print("We take: %d" % self.nums[row_index - 1])
                col_index = col_index - self.nums[row_index - 1]
                row_index = row_index - 1


if __name__ == '__main__':

    M = 9
    n = [2, 5, 3, 4, 1]

    problem = SubsetSum(n, M)
    problem.solve()
    problem.show_result()

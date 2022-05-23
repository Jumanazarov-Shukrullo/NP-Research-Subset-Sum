from solve import BruteForce, DynamicProgramming
from timeit import default_timer as timer
import approximation

def calculate_time():
    target = 100000000
    array = []
    size = len(array)
    epsilon = 0.2
    with open("data/numbers/numbers-100k.txt") as file:
        for line in file:
            line = line.strip()
            array.append(int(line))
    # start_br = timer()
    # b = BruteForce(size, target)
    # b.recursive_function(array, size, target)
    # end_br = timer()
    # print('Brute: ', end_br - start_br)
    # start_dp = timer()
    # d = DynamicProgramming(size, target)
    # d.solve(array, size, target)
    # end_dp = timer()
    # print('Dp: ', end_dp - start_dp)
    start_ap = timer()
    approximation.approximate_subset_sum(array, target, epsilon=epsilon)
    end_ap = timer()
    print(end_ap - start_ap)
calculate_time()

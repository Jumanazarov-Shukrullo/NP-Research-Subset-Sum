
from solve import BruteForce, DynamicProgramming, Memoization
from timeit import default_timer as timer
import matplotlib.pyplot as plt

br_list = []
dp_list = []
me_list = []

def calculate_time():
    for i in range(1, 18):
        target = 2000
        array = []
        size = len(array)
        with open("data/numbers/numbers-{}.txt".format(i)) as file:
            for line in file:
                line = line.strip()
                array.append(int(line))
        start_br = timer()
        b = BruteForce(size, target)
        b.recursive_function(array, size, target)
        end_br = timer()
        br_list.append(end_br - start_br)
        start_dp = timer()
        d = DynamicProgramming(size, target)
        d.solve(array, size, target)
        end_dp = timer()
        dp_list.append(end_dp - start_dp)
        start_me = timer()
        m = Memoization(size, target)
        m.solve(array, size, target)
        end_me = timer()
        me_list.append(end_me - start_me)

calculate_time()
x = [i for i in range(1, 18)]
plt.plot(x, br_list, label='Memoization')
plt.plot(x, dp_list, label='Tabulation')
plt.plot(x, me_list, label='Brute Force')
print(br_list)
print(dp_list)
print(me_list)
plt.legend()
plt.show()
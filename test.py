import random
from termcolor import cprint
from solve import BruteForce, DynamicProgramming, Memoization

size = []
target_sum = []


def generate_random_elements():
    for i in range(100):
        if i < 10:
            size.append(random.randint(50, 100))
            target_sum.append(random.randint(50, 150))
        else:
            size.append(random.randint(100, 150))
            target_sum.append(random.randint(150, 200))
    return size, target_sum


def generate_random_arrays(size):
    random.seed()
    array = []
    for i in range(1, size + 1):
        r = random.random()
        while round(r * 1000) == 0:
            r = random.random()
        array.append(round(r * 1000))
    return array


def test():
    counter = 0
    generate_random_elements()
    cprint("------Running Tests------", "blue")
    for i in range(50):
        s = size[i]
        t_sum = target_sum[i]
        brute_force = BruteForce(s, t_sum)
        dp = DynamicProgramming(s, t_sum)
        memo = Memoization(s, t_sum)

        brute_force_sol = brute_force.recursive_function(generate_random_arrays(s), s, t_sum)
        dp_sol = dp.solve(generate_random_arrays(s), s, t_sum)
        memo_sol = memo.solve(generate_random_arrays(s), s, t_sum)
        if brute_force_sol == dp_sol or brute_force_sol == memo_sol:
            counter += 1
            cprint("------ TEST PASSED: DYNAMIC PROGRAMMING -----", "green")
            cprint("------ TEST PASSED: Memoization -----", "green")
        else:
            cprint("------ TEST FAILED: DYNAMIC PROGRAMMING -----", "red")
            cprint("Got: {}".format(dp_sol), "red")
            cprint("Expected: {}".format(brute_force_sol), "cyan")
            cprint("------ TEST FAILED: Memoization -----", "red")
            cprint("Got: {}".format(memo_sol), "red")
            cprint("Expected: {}".format(brute_force_sol), "cyan")
            cprint("Failed in test №= {}".format(i), "yellow")

    cprint("Total: {}, failed: {}, passed: {}".format(int(50), int(50) - counter, counter), "blue")


if __name__ == "__main__":
    test()
# NP-Research-Subset-Sum

## Introduction
  The subset sum problem (SSP) is a decision problem in computer science. In its most general formulation, there is a multiset **S** of integers
  and a target-sum **T**, and the question is to decide whether any subset of the integers sum to precisely equal to **T**.\
  SSP can also be regarded as an optimization problem: find a subset whose sum is at most T, and subject to that, as close as possible to T.\
  SSP is a special case of the [knapsack](https://en.wikipedia.org/wiki/Knapsack_problem) problem and of the [multiple subset sum](https://en.wikipedia.org/wiki/Multiple_subset_sum) problem.
  
  The algorithm helps in introducing a class of discrete probability distributions which are useful in a sampling survey of populations, in constructing probability       models describing texture images, etc. It can also be used in integer programming, cryptography, and some other problems.
## Algorithm Complexity
  The problem is NP-complete. Furthermore there are some of its variants which are also NP-complete too:
  + The variant in which all inputs are positive.
  + The variant in which inputs may be positive or negative.
  + The variant in which all inputs are positive, and the target sum is exactly half the sum of all inputs. This special case of SSP is known as the partition problem.

The run-time complexity of SSP depends on two parameters:
+ n - the number of input integers and L - the precision of the problem.

When both n and L are large, SSP is NP-hard. The complexity of the best known algorithms is exponential in the smaller of the two parameters n and L. The problem is NP-hard even when all input integers are positive.

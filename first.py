# The naive algorithm by recursion in exponential time complexity

# The function SubSetSum returns true if there is a
# subset of given array with sum equal to target_sum

def SubSetSum(arr, size_, target_sum_):
    # if target_sum is zero  return true
    if target_sum_ == 0:
        return True
    # if size is zero then return false
    if size_ == 0:
        return False

    # Consider the last element and  the required_sum = target_sum – value of ‘last’ element
    # and number_of_elements = total_elements – 1
    # Leave the ‘last’ element and now required_sum = target_sum
    # and number_of_elements = total_elements – 1

    # if last element is greater than sum then we'll ignore it
    if arr[size_ - 1] > target_sum_:
        return SubSetSum(arr, size_ - 1, target_sum_)
    # else, check if target_sum can be obtained
    # by any of the following
    return SubSetSum(arr, size_ - 1, target_sum_) or SubSetSum(arr, size_ - 1, target_sum_ - arr[size_ - 1])


array = [1, 2, 4, 5, 6]
target_sum = 30
size = len(array)
if SubSetSum(array, size, target_sum):
    print("There is a subset with given target sum.\n")
else:
    print("There is not a subset with given target sum.\n")

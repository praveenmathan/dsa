# Problem: Given an array of integers, 
# find the maximum sum of a subarray with a fixed window size.

"""
1. determine the fixed window size
2. initialise and process
3. slide the window 
4. update and evolve 
5. continue sliding 
6. return result
"""

def maximum_sum_subarray_fn(arr, k):
    maximum_sum_in_a_subarray = 0
    current_sum = 0
    n = len(arr)

    # handle edge cases

    # find the current sum and initially assign to maximum_sum_in_a_subarray variable
    for i in range(k):
        current_sum = current_sum + arr[i]
    maximum_sum_in_a_subarray = current_sum

    #move the window by subtracting the left element and add the right element
    for i in range(k,n):
        current_sum = current_sum - arr[i-k] + arr[i]
        maximum_sum_in_a_subarray = max(maximum_sum_in_a_subarray, current_sum)
    
    return maximum_sum_in_a_subarray

if __name__ == '__main__':
    fixed_window_size = 3
    array = [2,1,3,4,5]
    result = maximum_sum_subarray_fn(array, fixed_window_size)
    print('Maximum sum from the subarray', result)
    print('Excecuted successfully')
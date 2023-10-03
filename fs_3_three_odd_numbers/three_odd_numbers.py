def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """

     # Iterate through nums using a sliding window of size 3
     #range below helps so that loop doesnt go out of bounds and stops when there is 3 elements left
    for i in range(len(nums) - 2):
        sequence_sum = nums[i]+ nums[i+1] + nums[i+2]
        if sequence_sum % 2 != 0:
            return True
        #if no odd sum is found
    return False
    


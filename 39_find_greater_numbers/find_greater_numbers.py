def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    # comparing the 1st index on the outer loop and second index on the inner loop with all other nums
    count = 0
    #range start from (0- start,end, step)
    for i in range(len(nums)):
        current_num =nums[i]
        for j in range(i + 1, len(nums)):
            next_num = nums[j]
            if current_num < next_num:
                count += 1
    return count


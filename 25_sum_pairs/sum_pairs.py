def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """

    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] + nums[j] == goal:
    #             return (nums[i], nums[j])
    # return ()  # returning empty tuple

    already_visited = {} #to keep track of numbers seen throught the iteration of nums

    for num in nums:
        difference = goal- num 

        if difference in already_visited:
            return (difference, num) # difference + num = goal
        else:
            already_visited.add(num)

    return ()


# The pair (5, 2) will be identified as a match for the goal before the pair (4, 3) is. When i is at index 0 (number 5), it will pair with j at index 5 (number 2) before i moves to index 2 (number 4).

# So, (5, 2) is indeed the first pair found that sums to 7, and that's what the function will return with the current logic. The explanation provided was inaccurate regarding that aspect, and I apologize for the confusion.

# If you'd like to get the result (4, 3) as the answer, the logic would need to be adjusted. The current logic gives the first pair in the order they appear in the list, but not necessarily the first pair of numbers that are positioned closest together.

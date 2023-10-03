def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
    unique_set = set()
    # if the num is not in the set then that number is the duplicate
    for num in nums:
        if num in unique_set:
            return num
        if num not in unique_set:
            unique_set.add(num)
    # returns None if no explicit return
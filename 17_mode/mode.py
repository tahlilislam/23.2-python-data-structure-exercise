def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    num_counter = {}
    for num in nums:
        num_counter[num] = num_counter.get(num, 0) + 1
    
     # find the highest value (the most frequent number)
    max_value = max(num_counter.values())

    # find the key that has most value
    for (key,value) in num_counter.items():
        if value ==max_value:
            return key
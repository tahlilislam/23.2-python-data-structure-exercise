def last_element(lst):
    """Return last item in list (None if list is empty.

        >>> last_element([1, 2, 3])
        3

        >>> last_element([]) is None
        True
    """
    if isinstance(lst, list):
        if not lst:
            return None
        return lst[-1]
    return "This function only works on list data types"

#function return None by default so didnt need to do the not lst boolean check
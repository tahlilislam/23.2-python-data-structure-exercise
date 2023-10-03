def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    return [item for item in lst if item]
    #could have also used a loop and initialized an empty list to hold the items from the loop

    

#     return [item for item in lst if item== True]

# The expression item == True checks if the item is explicitly equal to True. 
# Most of the "truthy" items in Python are not the boolean value True but 
# they still evaluate to True in a boolean context.
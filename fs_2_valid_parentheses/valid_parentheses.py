def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    # Python does not have a distinct data type for stacks; 
    # they are implemented using lists with specific usage patterns. 
    # When you use a list as a stack and only perform append() and pop() operations, 
    # you are effectively utilizing it as a stack, following the LIFO behavior.
    
    # Initializing an empty stack
    stack = []

    for p in parens:
        if p == "(":
            stack.append(p)
        elif p == ")":
            # Check if the stack is empty before popping
            if not stack:
                return False
            stack.pop()

    if not stack:
        return True
    return False


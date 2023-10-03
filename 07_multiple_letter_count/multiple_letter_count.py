def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    # return {char: phrase.count(char) for char in phrase} #dictionary comprehension
    #  approach less efficient for larger strings have to loop over each time taking time

    counter = {}

    for char in phrase:
        counter[char] = counter.get(char,0) + 1
    return counter


# creating a frequency dicitonary to get total fequency of all digits
# the dictionary should match
def get_freq_dict(num_str):
    return {digit: num_str.count(digit) for digit in set(num_str)}


def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    str_num1 = str(num1)
    str_num2 = str(num2)

    return get_freq_dict(str_num1) == get_freq_dict(str_num2)



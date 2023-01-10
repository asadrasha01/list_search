def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    odd_num = [n for n in data if n%2 != 0]
    return max(odd_num) if odd_num else 0
def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    odd_num = [n for n in data if n%2 != 0]
    return min(odd_num) if odd_num else 0
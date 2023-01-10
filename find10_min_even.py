def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    even_num = [n for n in data if n%2 == 0]
    return min(even_num) if even_num else 0
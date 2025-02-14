def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    even_num = [n for n in data if n%2 == 0]
    return max(even_num) if even_num else 0
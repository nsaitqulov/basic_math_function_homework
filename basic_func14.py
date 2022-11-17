def main(a, b):
    '''find the floor division of a and b and return it.
    
    Args:
        a (int): a number
        b (int): a number
        
    Returns:
        int: the result.
    '''
    import math
    x=math.floor(a/b)
    return x
print(main(11, 2))
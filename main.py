from datetime import datetime
import time


# Part 1
def clock(n):
    # Your code here
    """
    shows time which updates once every second for n seconds

    Parameters
    ----------
    n
        number of seconds

    Returns
    -------
    time
        time in HH:MM:SS format without milliseconds

    Example:
    >>> clock(3)
    12:59:17
    """
    while n >= 1: 
        dt = datetime.now()
        hhmmss = (str(dt.hour) +':'+ str(dt.minute)+':' +str(dt.second))
        n -= 1
        print(hhmmss, end ='\r')
        time.sleep(1)
    pass
# Part 2
def lcm(a, b):
    # Your code here
    """
    calculate lowest common multiple of two integers a and b

    Parameters
    ----------
    a
        first integer
    b
        second integer

    Returns
    -------
    lcm
        lowest common multiple of a and b

    Example:
    >>> lcm(2, 3)
    6
    >>> lcm(12, 5)
    60
    """
    a_ori = a
    b_ori = b
    while a != b:
        if a < b:
            a += a_ori
        elif b < a:
            b += b_ori
    return a


# Part 3
def gcf(a, b):
    # Your code here
    """
    calculate greatest common factor of positive integers a and b

    Parameters
    ----------
    a
        first positive integer
    b
        second positive integer

    Returns
    -------
    gcf
        greatest common factor of a and b
    """
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
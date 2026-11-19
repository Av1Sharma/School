"""
A module devoted to exceptions and dynamic typing

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""
import datetime

# PART 1
def is_date(year, month, day):
    """
    Returns True if the three integers form a valid date.
    
    Note that a year has to be nonzero for it to be valid.
    
    Examples: is_date(2023,2,29) returns False
              is_date(2024,2,29) returns True
    
    Parameter year: The candidate year
    Precondition: year is an int
    
    Parameter month: The candidate month
    Precondition: month is an int
    
    Parameter day: The candidate month
    Precondition: day is an int
    """
    from datetime import date
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False

# PART 2
def get_previous(filename):d
    """
    Returns the number before the one stored in the file filename.

    By number before, we mean that the number is an int, and the result subtracts one
    from the int in the file.

    If the file does not contain an int, this function returns the contents of the file.

    If the file does not exist or cannot be opened, this function returns None.

    Parameter filename: The name of the file to open
    Precondition: filename is a string
    """
    assert isinstance(filename, str), 'filename must be a string'

    try:
        with open(filename) as file:
            contents = file.read()
    except OSError:
        return None

    try:
        return int(contents) - 1
    except ValueError:
        return contents


# Part 3
# IMPLEMENT A NEW EXCEPTION CALLED LimitedUnavailableError HERE



class Limited(object):
    """
    A class that only allows you to make a limited number of objects.

    This class has a class attribute named AVAILABLE.  Every time an object is
    created, this attribute is decremented by one.  When each reaches 0, no more
    objects can be created.  Further constructor calls will raise a
    LimitedUnavailableError.

    INSTANCE ATTRIBUTE:
        x: A simple number [int or float]
    """

    # How many objects are left (starts at 4)
    AVAILABLE = 4

    def __init__(self,x):
        """
        Initializes a new Limited object

        The initializer checks to see if the object can be created (is AVAILABLE > 0).
        If so, it creates  a new object with attribute x and decrements AVAILABLE by 1.
        Otherwise, it raises a LimitedUnavailableError with x as the error.

        Parameter x: The object x value
        Precondition: x is an int or float
        """
        # IMPLEMENT ME
        pass


# Part 3
class Point2(object):
    """
    A class to represent a point in 2D space

    Attribute x: the x-coordinate
    Invariant: x is a float

    Attribute y: the x-coordinate
    Invariant: y is a float
    """

    def __init__(self,x,y):
        """
        Initializes a new Point

        Parameter x: The x-coordinate
        Precondition: x is a float

        Parameter y: The y-coordinate
        Precondition: y is a float
        """
        assert type(x) in [int,float], '%s is not a number' % repr(x)
        assert type(y) in [int,float], '%s is not a number' % repr(y)
        self.x = x
        self.y = y

    def __eq__(self,other):
        """
        Returns True if other is an instance of Point2 and equal to this one.

        Two points are equivalent if they share the same x and y values.

        Parameter other: The object to compare
        Precondition: other can be anything
        """
        # IMPLEMENT ME
        pass

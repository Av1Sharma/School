## Not really an excerise just an example

## Displays that u can use another function to display a function:


def uses_none(word, forbidden):
    """Checks whether a word avoids forbidden letters.
    
    >>> uses_none('banana', 'xyz')
    True
    >>> uses_none('apple', 'efg')
    False
    >>> uses_none('', 'abc')
    True
    """
    return not uses_any(word, forbidden)


## IMO, I think is highly messy and unorganized
## I would just not write this function at all and continue to use uses_any
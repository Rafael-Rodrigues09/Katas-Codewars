def min_max(lst):
    # the exercice's doesn't require a validation code, but I decide to add it for make a robust function
    if not lst or not isinstance(lst, list):
        return 'Type a valid input(list) && a non empty list'
    return [min(lst), max(lst)]



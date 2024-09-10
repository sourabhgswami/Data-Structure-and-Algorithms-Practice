def find_minimum(lst):
    minimum_element = lst[0]

    for value in lst:
        if minimum_element < value:
            minimum_element = value 
    
    return minimum_element
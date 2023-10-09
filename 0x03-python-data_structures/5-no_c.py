#!usr/bin/python3
def no_c(my_string):
    if not my_string:  # Check if the input string is empty
        return my_string  # Return the empty string as-is
    new_str = ' '
    for x in my_string:
        if x != 'c' and x != 'C':
            new_str += x
    return (new_str)

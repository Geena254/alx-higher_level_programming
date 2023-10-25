#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if not my_list:  # Check if my_list is empty
        return 0

    printed_count = 0

    try:
        for i in range(x):
            print(my_list[i], end="")
            printed_count += 1
    except (IndexError, TypeError):
        pass  # Catch exceptions for out-of-bounds index or type errors

    print()  # Print a new line after all elements

    return printed_count

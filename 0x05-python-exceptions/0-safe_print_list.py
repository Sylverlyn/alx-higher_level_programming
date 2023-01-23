#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    list = 0

    for i in range(x):
        try:
            print(f'{my_list[i]}', end='')
            list += 1
        except IndexError:
            pass

    print()
    return list

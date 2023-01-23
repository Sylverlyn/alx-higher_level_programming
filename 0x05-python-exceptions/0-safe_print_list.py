#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    list = 0
<<<<<<< HEAD

=======
>>>>>>> 96b3d4afc8e48ad43b0e25245c149f34d5e26cef
    for i in range(x):
        try:
            print(f'{my_list[i]}', end='')
            list += 1
<<<<<<< HEAD
=======

>>>>>>> 96b3d4afc8e48ad43b0e25245c149f34d5e26cef
        except IndexError:
            pass

    print()
<<<<<<< HEAD
    return list
=======
    return list
>>>>>>> 96b3d4afc8e48ad43b0e25245c149f34d5e26cef

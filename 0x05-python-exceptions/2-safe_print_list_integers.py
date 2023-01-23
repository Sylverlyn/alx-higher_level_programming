def safe_print_list_integers(my_list=[], x=0):
    list = 0	
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            list += 1	

        except Exception:
            pass
    print()
    return list	

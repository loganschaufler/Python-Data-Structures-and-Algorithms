def is_pal(str):
    l = len(str)

    if l < 2:
        return True

    elif str[0] == str[l - 1]:
        return is_pal(str[1: l - 1])
 
    else:
        return False
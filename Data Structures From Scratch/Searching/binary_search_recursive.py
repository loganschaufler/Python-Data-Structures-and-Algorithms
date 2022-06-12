def binary_search_rec(a_list, item):
	if len(a_list) == 0:
	    return False
	else:
	    midpoint = len(a_list) // 2
	    if a_list[midpoint] == item:
	        return True
	    elif item < a_list[midpoint]:
	        return binary_search_rec(a_list[:midpoint], item)
	    else:
	        return binary_search_rec(a_list[midpoint + 1 :], item)
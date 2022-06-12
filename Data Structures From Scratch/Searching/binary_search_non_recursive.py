def binary_search(a_list, item):
	first = 0
	last = len(a_list) - 1
	
	while first <= last:
	    midpoint = (first + last) // 2
	    if a_list[midpoint] == item:
	        return True
	    elif item < a_list[midpoint]:
	        last = midpoint - 1
	    else:
	        first = midpoint + 1
	
	return False
def sequential_search(a_list, item):
	pos = 0
	
	while pos < len(a_list):
	    if a_list[pos] == item:
	        return True
	    else:
	        pos = pos + 1
	
	return False
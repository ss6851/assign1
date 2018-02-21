def parse(CONTENT):
    my_list = CONTENT.split("\n")
    first_line = my_list[0]
    return first_line

def get_input(CONTENT):
    input = CONTENT.split("&")
    '''
    list_of_input=[]
    for i in input:
        list_of_input.append(i.split("="))
    return list_of_input
	'''    
    list_of_keys=[]
    for i in input:
    	list_of_keys.append(i.split("=")[0])

    list_of_values=[]
    for i in input:
    	list_of_values.append(i.split("=")[1])

    dict_of_input={}
    for i in range(len(list_of_keys)):
    	dict_of_input[list_of_keys[i]] = list_of_values[i]

    return list_of_values
    #return dict_of_input    


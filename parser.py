def parser(CONTENT):
    my_list = CONTENT.split("\n")
    first_line = my_list[0]
    return first_line

def get_input(CONTENT):
    input = CONTENT.split("&")
    list_of_input=[]
    for i in input:
        list_of_input.append(i.split("="))
    return list_of_input

#get_input("Name=Abulfazl&LastName=Jalaly&UserName=abcd&Password=1234567890")
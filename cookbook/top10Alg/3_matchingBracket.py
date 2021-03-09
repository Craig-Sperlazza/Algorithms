#matching bracket problem

#approach: create a stack

def balance_bracket (str_obj):
    #first we split the string into a list
    new_list = str_obj.split(" ")
    
    #create an empty stack object
    stack_obj = []

    #iterate through the list appending opening items
    for i in new_list:
        if i == "[" or i == "{" or i == "(":
            stack_obj.append(i)
        
        #for the string to be balanced if it is a closing item ("}})"), the last item appended to the list
        #must by the opening item of the matching type and we pop off if it is a matching pair
        else:
            if i == "]":
                if stack_obj[-1] == "[":
                    stack_obj.pop()
                else:
                    return "Not Balanced 1"
            if i == "}":
                if stack_obj[-1] == "{":
                    stack_obj.pop()
                else:
                    return "Not Balanced 1"
            if i == ")":
                if stack_obj[-1] == "(":
                    stack_obj.pop()
                else:
                    return "Not Balanced 1"
    return "Balanced"
                    
        


if __name__ == "__main__":
    exp1 = "[ ( ) ] { } { [ ( ) ( ) ] ( ) }"
    #Output: Balanced

    exp2 = "[ ( ] )"
    #Output: Not Balanced 

    exp3 = "{()}[]"
    # Output: Balanced

    print(balance_bracket(exp1))
    print(balance_bracket(exp2))
    print(balance_bracket(exp3))

def multiply(any_list):
    
    x = any_list.count('*')
    while x > 0:
        i = any_list.index("*")
        if any_list[i] == "*":
            mult = int(any_list[i-1])*int(any_list[i+1])
            any_list.pop(i-1)
            any_list.pop(i-1)
            any_list[i-1] = mult
            x -=1
        
    return any_list

def grst(a,b,c):
    if(a>b and a>c):
        return a
    elif(c>a and c>b):
        return c
    else:
        return "all equal"
    
print(grst(3,56,76))
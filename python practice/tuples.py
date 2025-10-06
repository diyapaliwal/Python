# how to append in tuple
t = (1,2,3,4)
temp = list(t)
temp.append(5)
t = tuple(temp)
print(t)

a = (1)    # writing one alone may confuse python an give <class 'int'>
a =(1,) # this will make it look like a tuple
print(type(a))

b = (1,34,7767,"djuyt",767,"sds") 
# b[0]= 5 # error
print(b)
# tuples are immutable just like strings but lists are mutable

no = b.count(34)
print(no)
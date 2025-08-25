s = {8,7,12,"Harry",[1,2]}
s[4] = [2,2]  
# cant update a list in a set because set do not allow indexing

#and we cant have list in a set

print(s)  
# error will be printed

# A set in Python only stores hashable (immutable) objects.

# A list is mutable (its elements can be changed).

# Because lists can change, Python can’t assign them a fixed hash value.

# Without a hash, a list can’t be added into a set.
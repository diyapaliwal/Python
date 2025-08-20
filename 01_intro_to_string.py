name = "Manisha"
print(len(name))

# slicing
nameshort = name[0:4] #start from index 0 and go till index 3(excluded)
print(nameshort)

# -ve slicing
print(name[-4:-1])
print(name[:4])  # is same as print(name[0:4])
print(name[1:])  # is same as print(name[1:7])
print(name[1:7])

# slicing with skip value
print(name[1:7:2])
import os
# select the path to list contents
path = "/New folder"

# List and print contents
contents = os.listdir(path)
print("Contents of the directory:")

# Iterate through the contents and print each item
for item in contents:
    print(item)

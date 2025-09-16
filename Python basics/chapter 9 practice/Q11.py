# Write a python program to rename a file to “renamed_by_ python.txt".

# this work can easily be done by os module in python 

import os

old_name = "Q11_old.txt"
new_name = "Q11_renamed_by_python.txt"

os.rename(old_name,new_name)
# os.rename(new_name,old_name)
print("file renamed succesfully!")
'''
a = "a very long string with emails"
emails = []
it takes 3 sec to run the code and the data output persists in ram and vanishes soon.

The random-access memory is volatile, and all its contents are lost once a program
terminates. In order to persist the data forever, we use files.

A file is data stored in a storage device. A python program can talk to the file by reading
content from it and writing content to it.
'''

f = open("file.txt") # dont need to write open("file.txt", "r") because open by default have r as default mode
data = f.read()
print(data)
f.close()   # important (its a duety to close the opened file sot that next files can access a closed file.)

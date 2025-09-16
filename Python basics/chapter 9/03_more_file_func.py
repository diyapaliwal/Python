f = open("file.txt")
lines = f.readlines()   # readlines
print(lines, type(lines))
print(lines[3], type(lines))
f.close()

f = open("file.txt")
lines = f.readline()   # readlone
print(lines, type(lines))
print(lines[0], type(lines))
print(lines[1], type(lines))
print(lines[2], type(lines))
print(lines[3], type(lines))
f.close()
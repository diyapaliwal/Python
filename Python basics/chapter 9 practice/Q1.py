st = '''Twinkle, twinkle, little star

How I wonder what you are

Up above the world so high

Like a diamond in the sky

Twinkle, twinkle little star

How I wonder what you are'''
f = open("Q1_poems.txt","w")
f.write(st)
f.close()

with open("Q1_poems.txt") as f:
    poem= f.read()
    if "twinkle" in poem.lower() :
        print("Yes!")
    else:
        print("No!")
        
    print(poem.lower().count("twinkle"))
        
    f.close()
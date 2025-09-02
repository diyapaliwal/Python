# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old.
def gt():
    table = ""
    for j in range(1,11):
        table +=(f"{i}*{j}={i*j} \n")
        
    with open(f"13_yr_old/table_{i}.txt","w") as f:
        f.write(table)
    
for i in range(2,21):
    gt()
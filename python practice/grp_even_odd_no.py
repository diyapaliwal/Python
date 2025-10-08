# group even and odd numbers
nums = [1,2,3,4,5,6]

def grp(num):
    even=[]
    odd=[]
    for n in num:
        if n%2 == 0:
            even.append(n)
            
        else:
            odd.append(n)
        
    print(odd)
    print(even)
        
grp(nums)
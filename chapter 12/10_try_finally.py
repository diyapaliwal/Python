def main():
    try:
        a = int(input("Enter a number: "))
        print(a)
        return
    
    except Exception as e:
        print(e)
        return   
    
    finally:
        print("hey I am inside of finally.")
        
main()
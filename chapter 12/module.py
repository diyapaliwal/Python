def myFunc():
     print("Hello World!")
     
if __name__ == "__main__":
# if code runs directly by running the file its written in
     print("We are directly running this code")
     myFunc()
     print(__name__)

     # this restricts the code to be teliported and only runs in the module file
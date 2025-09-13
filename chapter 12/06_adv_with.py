with (
    open ("chapter 12/File1.txt","w") as f1,
    open ("chapter 12/File2.txt","w") as f2
):
    f1.write("hello f1")
    f2.write("hello f2")
# using walrus operator " := "
if (n := len([1,2,456,6,7])) > 3:
    print(f"list is too long ({n} elements, expected <= 3)")
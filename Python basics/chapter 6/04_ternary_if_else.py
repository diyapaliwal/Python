age = 19
status = "adult" if age>=18 else "minor"
print(status)
'''The ternary operator, also known as the conditional operator, is a concise way to write an if-else statement in a single line. It evaluates a condition and returns one of two values based on whether the condition is true or false.
​Syntax
​The general syntax is:
​condition ? value_if_true : value_if_false
​condition: The expression to be evaluated.
​?: Separates the condition from the values.
​value_if_true: The value returned if the condition is true.
​:: Separates the two possible return values.
​value_if_false: The value returned if the condition is false.
'''
#[1, “a”, 2, “b”, 3, “c”] filter digits and alphabets separately using inbuilt functions like map, filter or reduce


def fun1(variable):
    variable=str(variable)
    return variable.isdigit()
def fun2(variable):
    variable=str(variable)
    return variable.isalpha()
sequence = [1, 'a', 2, 'b', 3, 'c']
filteredint = filter(fun1, sequence)
filteredalphabet = filter(fun2, sequence)

digits=[s for s in filteredint]
letters=[s for s in filteredalphabet]

print(digits)
print(letters)
    



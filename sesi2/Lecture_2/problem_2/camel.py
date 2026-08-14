camel = input("camelCase: ")

print("snake_case: ", end="")

for x in camel:
    if x.isupper():
        print("_" + x.lower(), end="")
    else:
        print(x, end="")
print()


import inflect
names = []
p = inflect.engine()
while True: 
    try:
        name = input('Name: ')
    except EOFError:
        break
    names.append(name)
answer = p.join(names)
print(f"Adieu, adieu, to {answer}")

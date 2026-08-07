word = input("Input: ")

print("Output: ", end="")
for x in word:
    if x.lower() in "aiueo":
        print("" , end="")
    else:
        print(x, end="")

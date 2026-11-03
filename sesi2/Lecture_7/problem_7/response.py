import validators

email = input("What's your email address? ").strip()

new_email = validators.email(email)
if new_email == True:
    print("Valid")
else:
    print("Invalid")
    
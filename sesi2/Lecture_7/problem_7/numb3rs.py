import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))
    
def validate(ip):
   valid = re.search(r"^(0|[1-9]\d{0,2})\.(0|[1-9]\d{0,2})\.(0|[1-9]\d{0,2})\.(0|[1-9]\d{0,2})$", ip)
   if valid:
       number1 = int(valid.group(1))
       number2 = int(valid.group(2))
       number3 = int(valid.group(3))
       number4 = int(valid.group(4))
       if number1 > 255:
           return False
       if number2 > 255:
           return False
       if number3 > 255:
           return False
       if number4 > 255:
           return False
       return True
   else:
       return False
if __name__ == "__main__":
    main()
import sys 
import pyfiglet
import random
if len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit("Invalid usage")
if len(sys.argv) == 3:
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            sys.exit("Invalid usage")
        if sys.argv[2] not in pyfiglet.FigletFont.getFonts():
            sys.exit("Invalid usage")
if len(sys.argv) == 1:
    the_font = random.choice(pyfiglet.FigletFont.getFonts())
else:
    the_font = sys.argv[2]
    
text = input("Input: ")

print(pyfiglet.figlet_format(text, font=the_font))
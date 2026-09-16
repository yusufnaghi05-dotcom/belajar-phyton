import sys 
import pyfiglet
import random
if len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit()
if len(sys.argv) == 3:
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            sys.exit()
        if sys.argv[2] not in pyfiglet.FigletFont.getFonts():
            sys.exit()
if len(sys.argv) == 1:
    font = random.choice(pyfiglet.FigletFont.getFonts())
else:
    font = sys.argv[2]

import sys
from PIL import Image
import os

file_name = os.path.splitext("before.jpg")
first_file_name = file_name[0]
second_file_name = file_name[1]

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if sys.argv[1].endswith(".png") or sys.argv[2].endswith(".png"):
    sys.exit("Input and output have different extensions ")
    
try:
    
    
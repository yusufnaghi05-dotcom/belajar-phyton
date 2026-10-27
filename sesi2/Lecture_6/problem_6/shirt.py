import sys
import os
from PIL import Image
from PIL import ImageOps
import PIL

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]

allowed_extensions = (".jpg", ".jpeg", ".png")

input_ext = os.path.splitext(input_file)[1].lower()
output_ext = os.path.splitext(output_file)[1].lower()

if input_ext not in allowed_extensions or output_ext not in allowed_extensions:
    sys.exit("Invalid input or output")

if input_ext != output_ext:
    sys.exit("Input and output have different extensions")
    
try:
    photo = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")
    size = shirt.size
    new_photo = ImageOps.fit(photo, size)
    new_photo.paste(shirt, mask=shirt)
    new_photo.save(sys.argv[2])
    
except FileNotFoundError:
    sys.exit("Input does not exist")
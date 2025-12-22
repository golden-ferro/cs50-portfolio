from PIL import Image, ImageOps
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

input_path = sys.argv[1]
output_path = sys.argv[2]

if not input_path.lower().endswith((".jpg", ".jpeg", ".png")):
    sys.exit("Invalid input")

if not output_path.lower().endswith((".jpg", ".jpeg", ".png")):
    sys.exit("Invalid output")

try:
    with open(input_path, "rb") as file:
        input_image = Image.open(file).convert("RGBA").copy()

    with open("shirt.png", "rb") as file:
        shirt = Image.open(file).convert("RGBA").copy()

except FileNotFoundError:
    sys.exit("File does not exist")

input_ext = input_path.split('.')[-1].lower()
output_ext = output_path.split('.')[-1].lower()

if input_ext != output_ext:
    sys.exit("Input and output have different extensions")

input_resized = ImageOps.fit(input_image, shirt.size)

input_resized.paste(shirt, (0, 0), shirt)

if output_path.lower().endswith((".jpg", ".jpeg")):
    input_resized.convert("RGB").save(output_path, "JPEG")
elif output_path.lower().endswith(".png"):
    input_resized.save(output_path, "PNG")



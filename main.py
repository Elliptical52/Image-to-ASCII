import random
import numpy as np
from PIL import Image

width = 64
height = 64
input_path = "bliss.png"


characters = " -':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"

RESET = "\x1b[0m"

image = Image.open(input_path).convert("RGBA")
image = image.resize((width, height))

image_array = np.array(image)


output_string = ''

for y in range(height):
    for x in range(width):
        r, g, b, a = image_array[y, x]

        color_code = f'\x1b[38;2;{r};{g};{b}m'
        brightness = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255
        index = int(brightness * (len(characters) - 1))
        character = characters[index]
        output_string += color_code + character * 2
    output_string += '\n'



print(output_string)

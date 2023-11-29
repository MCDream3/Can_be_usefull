import getopt
import sys
from math import ceil, sqrt
from PIL import Image

def main(argv):
    if len(argv) != 2:
        print('usage: main_decode.py [INPUT_FILE] [OUTPUT_FILE]')
        sys.exit(2)

with open(argv[0], 'r') as f:
    input = f.read()

bits_count = len(input) * 8
size = int(ceil(sqrt(bits_count)))
image = Image.new("RGB",(size,size), "black")
pixels = image.load

x = 0
y = 0
white = (255,255,255)
for ch in input:
    value = ord(ch)
    for i in range(8):
        bit = (value >> (7 - i)) & 1
        if bit == 1:
            pixels[x,y] = white
        x += 1
        if x >= size:
            x = 0
            y += 1
    image.save(argv[1], 'jpg')

if __name__ == '__main__':
    main(sys.argv[1:])

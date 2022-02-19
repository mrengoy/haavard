import PIL
from PIL import Image
from numpy import outer
import requests
from io import BytesIO


f = open("./graf.png", "rb")
img = Image.open(BytesIO(f.read()))
print(img.size)
print(img.mode)
print(img.getpixel((0,0)))


pix_width = img.size[0]
pix_height = img.size[1]

X = 10
Y = 10

step_size_x = int(pix_width / (X + 2))
step_size_y = int(pix_height / (Y + 2))

output = []

# Legg inn hex verdier her
colors = ["240090", 
"240090", 
"3701fe", 
"01d6f2",
"017183",
]

for x in range(1, X):
    for y in range(1, Y):

        output.append(img.getpixel((x,y)))

print(output)
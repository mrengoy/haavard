import PIL
from PIL import Image
from numpy import outer
import requests
from io import BytesIO


f = open("./graf.png", "rb")
img = Image.open(BytesIO(f.read()))
print(img.size)
print(img.mode)
print(type(img.getpixel((0,0))))


pix_width = img.size[0]
pix_height = img.size[1]

X = 100
Y = 100

step_size_x = int(pix_width / (X + 2))
step_size_y = int(pix_height / (Y + 2))

output = []


# Her er de vanligste fargene sortert, med (r,g,b,a) : antall-tilfeller
# Kan du gå gjennom og erstatte "antall-tilfeller" med verdien til fargen i grafen?
color_map = {(134, 111, 201, 255): 6,
             (255, 29, 0, 255): 6,
             (92, 0, 0, 255): 6,
             (168, 0, 0, 255): 6,
             (238, 86, 0, 255): 7,
             (255, 23, 0, 255): 9,
             (240, 33, 0, 255): 9,
             (234, 0, 0, 255): 9,
             (0, 165, 255, 255): 14,
             (228, 0, 0, 255): 14,
             (242, 0, 0, 255): 16,
             (166, 0, 0, 255): 16,
             (202, 0, 0, 255): 16,
             (0, 226, 255, 255): 17,
             (249, 0, 0, 255): 18,
             (215, 0, 0, 255): 19,
             (156, 0, 0, 255): 19,
             (220, 0, 0, 255): 21,
             (246, 246, 246, 255): 21,
             (214, 0, 0, 255): 23,
             (0, 255, 243, 255): 24,
             (0, 255, 210, 255): 32,
             (254, 254, 254, 255): 39,
             (55, 0, 255, 255): 42,
             (0, 255, 161, 255): 42,
             (231, 231, 231, 255): 42,
             (197, 0, 0, 255): 48,
             (165, 0, 0, 255): 58,
             (84, 255, 109, 255): 59,
             (229, 229, 229, 255): 62,
             (225, 225, 225, 255): 68,
             (251, 251, 251, 255): 69,
             (141, 255, 72, 255): 74,
             (207, 255, 0, 255): 93,
             (251, 254, 0, 255): 116,
             (37, 0, 145, 255): 125,
             (255, 217, 0, 255): 141,
             (255, 159, 0, 255): 167,
             (255, 94, 0, 255): 212,
             (255, 26, 0, 255): 259,
             (171, 0, 0, 255): 835,
             (255, 0, 0, 255): 1054,
             (223, 0, 0, 255): 1177,
             (255, 255, 255, 255) : 3757
             }

# Get items
for x in range(1, X):
    for y in range(1, Y):
        output.append(img.getpixel((x*step_size_x,y*step_size_y)))

color_occurences = {}
# Count occurences
for c in output:
    color_occurences[c] = output.count(c)

most_important_colors = list(filter(lambda c: color_occurences[c] > 5, color_occurences.keys()))
for s in sorted(most_important_colors, key=lambda x: color_occurences[x]):
    print(str(s) + " : " + str(color_occurences[s]))

# for o in list(dict.fromkeys(output)):
#     #print(o)
#     r = o[0]
#     g = o[1]
#     b = o[2]
#     if (r != g or r != b):
#         pass
import os
import json
import re
from convert import handle_image_conversion

os.chdir("database")
# convert pokemon images to greyscale, remember to checkout the image directory before doing this
# os.system("mogrify -charcoal 1 -white-threshold 75% -blur 8 -black-threshold 90% images/*.jpg")

pkmns = None
with open("pokemons.json") as f:
    pkmns = json.load(f)

npkmns = {}

for img in os.listdir("images"):
    if img.endswith(".jpg"):
        pid = img[:-4]  # drop .jpg
        ascii = handle_image_conversion("images" + os.sep + img, new_width=30).replace("@", " ")
        npkmns[pkmns[pid]["name"]] = ascii

with open("pokemons_new.json", "w") as f:
    json.dump(npkmns, f)

print(npkmns["Bulbasaur"])

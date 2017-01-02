import os
import json
import re
from convert import handle_image_conversion

os.chdir("database")

pkmns = None
with open("pokemons.json") as f:
    pkmns = json.load(f)

# for img in os.listdir("images"):
#     if img.endswith(".jpg"):
#         pid = img[:-4]  # drop .jpg
#         ascii = handle_image_conversion("images" + os.sep + img, new_width=30).replace("#", " ")
#         pkmns[pid]["ascii"] = ascii

with open("pokemons.json", "w") as f:
    json.dump(pkmns, f)

print(pkmns["1"]["ascii"])
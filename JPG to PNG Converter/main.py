import sys
import os
from PIL import Image

# grab first and second argument
src_folder = sys.argv[1]
des_folder = sys.argv[2]

# check if new/ exists, if not create it
if not os.path.exists(des_folder):
    os.makedirs(des_folder)

# loop through Pokedex,
# convert images to png
# save to the new folder.

for image in os.listdir(src_folder):
    Image.open(os.path.join(src_folder, image)).save(
        os.path.join(des_folder, f"{os.path.splitext(image)[0]}.png"), format="png"
    )
from PIL import Image
import os

path = "img/x/"
for f in os.listdir("img/x/"):
    if f.endswith(".png"):
        split_f = f.split(".")
        name = split_f[0] + "r" + ".png"
        im = Image.open(path + f).convert("RGBA")
        im.resize((200, 300)).save("img/x/" + name, "PNG")

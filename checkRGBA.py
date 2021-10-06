from PIL import Image
def check():
    im = Image.open("transparent.png")
    print (im.mode)

check()
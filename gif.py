#change gif image color to white and black
from PIL import Image
import os, imageio

gifFileName = "‪C:\\Users\\acer\\Desktop\\girl.gif"
path = gifFileName[:-4]
os.mkdir(path)
gif = Image.open(gifFileName)
try:
	while True:
		current = gif.tell()
		gif.save(path + "\\" + str(current) + ".png")
		gif.seek(current + 1)
except EOFError:
	pass

pathlist = os.listdir(path)
im = []
images = []

for p in pathlist:
    newPath = os.path.join(path, p)
    im.append(Image.open(newPath).convert("L"))
    im[pathlist.index(p)] = im[pathlist.index(p)].point(lambda i: i > 128 and 255)
    im[pathlist.index(p)].save(newPath, "PNG")
    images.append(imageio.imread(newPath))

imageio.mimsave(path + '//girl.gif', images)

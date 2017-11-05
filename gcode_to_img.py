from PIL import Image

size = (1920, 1080)
img = Image.new("1", size, 255)
path = "C:\\Users\\acer\\Desktop\\test.ngc"
with open(path, "rt") as f:
    txt = f.read()

arrs = txt.split("\n")

for arr in arrs:
	ar = arr.split(" ")
	x, y = None, None
	if len(ar) != 1:
		ar = ar[1:]
		for a in ar:
			if a[0] == "X":
				x = int(float(a[1:]))
			elif a[0] == "Y":
				y = int(float(a[1:]))
		if x != None and y != None:
		    img.putpixel((x, y), 0)

filename = path.split("\\")[-1][:-4] +  ".jpg"
img.save(filename)
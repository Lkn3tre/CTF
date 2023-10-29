from PIL import Image

im= Image.new("RGB", (30, 30), 'white')
f = open("qrcode")

b = [line[:-1] for line in f]
pixels = im.load()
pi = []

for x in range(29):
    pi.append([int(d) for d in str(b[x])])
print(pi)
print(len(pi),len(pi[0]))
"""
for x in range(0,29):
	for y in range(0,29):
		if pi[x][y] == 1:
			pixels[x,y]=(0, 0, 0)
		else:
			pixels[x,y] = (255,255,255)
			
im = im.resize((1880, 1880), resample=Image.BOX)
im.show()
im.save("qr_code.jpg")
"""


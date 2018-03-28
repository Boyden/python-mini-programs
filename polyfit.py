import matplotlib.pyplot as plt
import numpy as np
import sys

#filePath = sys.argv[1]
filePath = "C:\\Users\\Administrator\\Desktop\\dataset"
with open(filePath, "rt") as f:
	content = f.read().split("\n\n")
	x1 = content[0].split("\n")
	y1 = content[1].split("\n")

	x2 = content[2].split("\n")
	y2 = content[3].split("\n")

	x3 = content[4].split("\n")
	y3 = content[5].split('\n')

x1_list = np.array(list(map(float, x1[1:])))
y1_list = np.array(list(map(float, y1[1:])))
x1_title = x1[0]
y1_title = y1[0]

x2_list = np.array(list(map(float, x2[1:])))   
y2_list = np.array(list(map(float, y2[1:])))
x2_title = x2[0]
y2_title = y2[0]


x3_list = np.array(list(map(float, x3[1:])))   
y3_list = np.array(list(map(float, y3[1:])))
x3_title = x3[0]
y3_title = y3[0]


z1 = np.polyfit(list(map(float, x1[1:])), list(map(float, y1[1:])), 1)
print(np.poly1d(z1))

z2 = np.polyfit(list(map(float, x2[1:])), list(map(float, y2[1:])), 1)
print(np.poly1d(z2))

z3 = np.polyfit(list(map(float, x3[1:])), list(map(float, y3[1:])), 1)
print(np.poly1d(z3))

plt.figure(1)
plt.title("Quantitative determination of protein")

plt01 = plt.subplot(131)
plt01.set_xlabel(x1[0])
plt01.set_ylabel(y1[0])
plt01.set_title("Lowry")

plt01.scatter(x1_list, y1_list)
plt01.scatter(0.1067, 0.2195)
plt01.annotate('Test solution\n (0.1067, 0.2195)', xy=(0.1067, 0.2195), xytext=(0.1067, 0.2195-0.1),
            arrowprops=dict(facecolor='black', shrink=0.05, width=0.5,headwidth=4),
            )
plt01.text(0, 0.4, y1_title+"=1.982*u+0.008031")
plt01.plot(x1_list,z1[0]*x1_list+z1[1])


plt02 = plt.subplot(132)
plt02.set_xlabel(x2[0])
plt02.set_ylabel(y2[0])
plt02.set_title("Ultraviolet")

plt02.scatter(x2_list, y2_list)
plt02.scatter(0.5588, 0.334)
plt02.annotate('Test solution\n (0.5588, 0.334)', xy=(0.5588, 0.334), xytext=(0.5588, 0.334-0.1),
            arrowprops=dict(facecolor='black', shrink=0.05, width=0.5,headwidth=4),
            )
plt02.text(0, 0.6, y2_title+"=0.5994*u-0.0009286")
plt02.plot(x2_list,z2[0]*x2_list+z2[1])

plt03 = plt.subplot(133)
plt03.set_xlabel(x3[0])
plt03.set_ylabel(y3[0])
plt03.set_title("Bradford")

plt03.scatter(x3_list, y3_list)
plt03.scatter(0.580, 0.427)
plt03.annotate('Test solution\n (0.580, 0.427)', xy=(0.580, 0.427), xytext=(0.580, 0.427-0.1),
            arrowprops=dict(facecolor='black', shrink=0.05, width=0.5,headwidth=4),
            )
plt03.text(0, 0.7, y3_title+"=0.6913*u+0.02622")
plt03.plot(x3_list,z3[0]*x3_list+z3[1])

plt.show()
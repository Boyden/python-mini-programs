import matplotlib.pyplot as plt
import numpy as np
import sys

filePath = sys.argv[1]
with open(filePath, "rt") as f:
    
z = np.polyfit(x, y, 1)
fun = np.poly1d(z)
print(fun)

plt.xlabel("OD620")
plt.ylabel("Glucose standard solution(0.1g/L)(mL)")
plt.title("Glucose standard curve")

plt.scatter(x, y)
plt.plot(x, 0.6658*x+0.01499)
plt.scatter(0.784, 0.6658*0.784+0.01499)
plt.scatter(1.311, 0.6658*1.311+0.01499)
plt.annotate('No.6 Tube (0.784, 0.537)', xy=(0.784, 0.6658*0.784+0.01499), xytext=(0.784-0.4, 0.6658*0.784+0.01499+0.2),
            arrowprops=dict(facecolor='black', shrink=0.05, width=0.5,headwidth=4),
            )
plt.annotate('No.7 Tube (1.311, 0.888)', xy=(1.311, 0.6658*1.311+0.01499), xytext=(1.311-0.2, 0.6658*1.311+0.01499-0.2),
            arrowprops=dict(facecolor='black', shrink=0.05, width=0.5,headwidth=4),
            )
plt.text(0, 1, "y=0.6658*x+0.01499")

plt.show()
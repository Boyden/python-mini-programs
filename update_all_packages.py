#automatically update all pypi packages to the latest version
import os

s = os.popen("pip list --outdate")

li = s.readline()

for i in range(len(li)):
	os.system("pip install --upgrade " + li[i].split('-')[0].split(" ")[0])

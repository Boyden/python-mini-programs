#automatically update all pypi packages to the latest version
import os, subprocess

out_bytes = subprocess.check_output(['pip','list', '--outdate'])
out_text = out_bytes.decode('utf-8')
li = out_text.split("\r\n")

for i in range(len(li)):
    os.system("pip install --upgrade " + li[i].split(' - ')[0].split(" ")[0])

import os, json, sys

input_list = sys.argv[1:]

path = input_list[0]
if len(input_list) < 2:
    out_file_name = "output.mp4"
else:
    out_file_name = input_list[1]

if "." not in out_file_name:
    out_file_name = out_file_name + '.mp4'

with open(path + "\\index.json", "rt") as f:
    file_info =f.read()

file_info_json = json.loads(file_info)
seg_num = len(file_info_json['segment_list'])

with open(path + "\\filelist.txt", "at") as f:
    for i in range(seg_num):
        f.write("file " + str(i) + ".blv\n")

os.chdir(path)
os.system("ffmpeg -f concat -i filelist.txt -c copy " + out_file_name)
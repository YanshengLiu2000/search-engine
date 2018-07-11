from os import listdir
import os
#put it into NSWSC(all original html files in it).Run it, and this script will delete all lines contain <herf></herf>tag. 
for file in listdir(os.path.dirname(__file__)):
    with open(file, 'r') as r:
        lines = r.readlines()
    with open(file, 'w') as w:
        for line in lines:
            if 'href=' in line:
                continue
            w.write(line)
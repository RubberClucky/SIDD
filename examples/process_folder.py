import os
from tqdm import tqdm
from re import X
from sidd import siddmain

dir = "c:\\imgtest4"
dupes = siddmain.DedupeImageDirWithBuckets(dir,4)

tqdm.write("All finished")
tqdm.write(str(len(dupes)))
for dupe in dupes: 
    os.remove(dupe)
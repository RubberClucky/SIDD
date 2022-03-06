import cv2
import os
import alive_progress

def CompareImage(original, dupe) -> bool:
    originalImg = cv2.imread(original)
    dupeImg = cv2.imread(dupe)
    
    if originalImg.shape[:2] == dupeImg.shape[:2]:
        difference = cv2.subtract(originalImg, dupeImg)
        b, g, r = cv2.split(difference)
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            return True
        else:
            return False

def DedupeImageDir(directory):
    dupeList = []
    dirList = os.listdir(directory)
    i = 1
    for current in dirList:
        print(f"Processing: {current} .. {i}/{len(dirList) - len(dupeList)} (Minus Duplicates)")
        othersList = [x for x in dirList if x != current]
        with alive_progress(len(othersList)) as bar:
            if current in dupeList:
                print("Skipping, this is a duplicate.")
                continue
            for suspect in othersList:
                currentPath = os.path.join(directory,current)
                suspectPath = os.path.join(directory,suspect)
                result = CompareImage(currentPath, suspectPath)
                if result == True:
                    dupeList.append(suspect)
                bar()
        i=i+1
    return dupeList
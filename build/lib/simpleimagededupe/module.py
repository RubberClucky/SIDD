class simpleimagededupe:

    import cv2
    import os
    import alive_progress as alp

    def __init__(self):
        self.selfAlive = self.alp.alive_bar
        return None

    def CompareImage(self, original, dupe) -> bool:
        originalImg = self.cv2.imread(original)
        dupeImg = self.cv2.imread(dupe)
        
        if originalImg.shape[:2] == dupeImg.shape[:2]:
            difference = self.cv2.subtract(originalImg, dupeImg)
            b, g, r = self.cv2.split(difference)
            if self.cv2.countNonZero(b) == 0 and self.cv2.countNonZero(g) == 0 and self.cv2.countNonZero(r) == 0:
                return True
            else:
                return False

    def DedupeImageDir(self, directory):
        dupeList = []
        dirList = self.os.listdir(directory)
        i = 1
        for current in dirList:
            print(f"Processing: {current} .. {i}/{len(dirList) - len(dupeList)} (Minus Duplicates)")
            othersList = [x for x in dirList if x != current]
            with self.selfAlive(len(othersList)) as bar:
                if current in dupeList:
                    print("Skipping, this is a duplicate.")
                    continue
                for suspect in othersList:
                    currentPath = self.os.path.join(directory,current)
                    suspectPath = self.os.path.join(directory,suspect)
                    result = self.CompareImage(currentPath, suspectPath)
                    if result == True:
                        dupeList.append(suspect)
                    bar()
            i=i+1
        return dupeList
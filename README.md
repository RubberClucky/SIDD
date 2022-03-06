# <img src="img/uaflag.jpg" height="20px"> Python - SIDD (Simple Image DeDuplication)


 
A small python library designed with a simple goal. To compare a bunch of images and find duplicates. This tool was originally designed to support the Ukrainian IT Army and activist efforts to subvert the Russian misinformation campigns. Some projects required automation to help filter through media that was being collected. Hence this was born. This library is a more refined approach than the original that was delivered, and I personally hope they find this new implementation helpful. Слава Україні

-------------------------------------------------------------------  

Types of deduplication available (see examples below):
- One to one deplucation. Compare two cv2 images.
- Directory analysis (multithreaded) with exact match. Every image is compared with every image in a directory and exact matches are identified. Slow by identifies exact matches.
- Directory analysis (multithreaded) with probablistic match. Directory listing is divided into "chunks". Each image is downsized and placed in a bucket by the most frequent data. Image is checked against other non-duplicates when added to the bucket. There is still an n^2 problem as the buckets grow, but this attempts to circumvent some of the problem by avoiding comparisons in the beginning. Try it! Might need a beefy processor for thousands of images! May also experience issues if every image is the same color (like a directory full of tweets).

-------------------------------------------------------------------

Interested in helping this project?
- Use it in the wild!
- Report Issues
- Fork and submit PRs

-------------------------------------------------------------------

Installation Instructions
```
pip install sidd
```

Examples

Performs a probablistic comparison of 2 images cv2 images.
```
import cv2
from sidd import siddcompares

current = cv2.imread("image1.jpg")
suspect = cv2.imread("image2.jpg")

comp_method = siddcompares.CompareImageProbability
match = siddcompares.CompareImage(current, suspect, comp_method)

if match == True:
    print("It's a match!")
```

Clean up a folder using bucketed probablistic matching. This is by far the quickest method but can be innacurate. Make sure you backup your files first and thoroughly test. If you're comparing thousands of images, use this.
```
import os
from sidd import siddmain

dir = "c:\\imgtest4"
dupes = siddmain.DedupeImageDirWithBuckets(dir,4)

for dupe in dupes: 
    os.remove(dupe)
```

-------------------------------------------------------------------  

***Questions? Create an issue and ask.***
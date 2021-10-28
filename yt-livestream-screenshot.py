import pafy
import cv2
import time
import os

url = "https://www.youtube.com/watch?v=J5-4ZYnlGYo"
video = pafy.new(url)
best = video.getbest(preftype="mp4")

# get metadata
title = video.title
author = video.author
videoid = video.videoid

if os.path.isdir(videoid):
  print("folder exist")
else:
  os.mkdir(videoid)


# write metadata
path = videoid+"/"+ videoid +".txt"
f = open(path, "w",encoding="utf-8")
f.write("title: {} \n".format(title))
f.write("author: {} \n".format(author))
f.write("videoid: {} \n".format(videoid))
f.close()


capture = cv2.VideoCapture(best.url)

while True:
    grabbed, frame = capture.read()

    #save img
    nowTime = time.strftime("%Y%m%d%H%M")
    cv2.imwrite(videoid+"/"+"%s.jpg" % nowTime, frame, [cv2.IMWRITE_JPEG_QUALITY, 98])

print("livestream stop")
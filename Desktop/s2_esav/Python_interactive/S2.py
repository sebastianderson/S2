import os
import numpy as np
print("Enter a number from 3 or 4 to do the commands in these exercises")
input1 = input()
if input1 == "3":
    print("In which size do you want to convert the video:720,480,320,160?")
    input2 = input()
    if input2 == "720":
        os.system("ffmpeg -i BBB_10.avi -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 BBB_720P2.avi")
    elif input2 == "480":
        os.system("ffmpeg -i BBB_10.avi -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 BBB_480p.avi ")
    elif input2 == "320":
        os.system("ffmpeg -i BBB_10.avi -vf scale=320:240,setsar=1:1 BBB_302X240.avi")
    elif input2 == "160":
        os.system("ffmpeg -i BBB_10.avi -vf scale=160:120,setsar=1:1 BBB_160X120.avi ")
    print("The files has been saved")
elif input1 == "4":
    os.system("ffmpeg -i BBB_10.avi -vn -acodec copy BBB-audio.mp4")
    os.system("ffmpeg -i BBB-audio.mp4 -ac 1 BBB-audio.wav")
    os.system("ffmpeg -i BBB_10.avi -i BBB-audio.wav -shortest -c:v copy -c:a aac -b:a 256k -ac 1 BBB_mono.avi")
    print("The files has been saved in BBB_mono.avi")

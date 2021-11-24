# coding=utf-8

# [requirement]
# pip install opencv-python
# pip install numpy

# [usage]
# python convert_vid_to_img_opencv.py a.mp4 save_first_frame
# python convert_vid_to_img_opencv.py a.mp4 save_all_frames
# python convert_vid_to_img_opencv.py a.mp4 save_last_frame_by_asc_traversing
# python convert_vid_to_img_opencv.py a.mp4 save_last_frame_by_desc_traversing
# python convert_vid_to_img_opencv.py a.mp4 save_middle_frame_by_desc_traversing
# python convert_vid_to_img_opencv.py a.mp4 20

import sys, os, shutil

import judger






def main():

    p1="https://ww3.sinaimg.cn/bmiddle/007INInDly1g336j2zziwj30su0g848w.jpg"
    p2="https://ww2.sinaimg.cn/bmiddle/007INInDly1g336j10d32j30vd0hnam6.jpg"
    judger.runAllImageSimilaryFun(p1,p2)



if __name__ == "__main__":
    main()

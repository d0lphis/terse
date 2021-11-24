# coding=utf-8

# [requirement]
# pip install opencv-python
# pip install numpy

# [usage]
# python add_thumbnail_to_vids_and_fix_incomplete_opencv_ffmpeg.py <folder_contain_vids_without_thumbnail>

import sys, os, shutil, subprocess
import cv2
import vidder






def main():
    classifications = {}
    VID_FOLDER_FULL_NAME = sys.argv[1]
    list = os.listdir(VID_FOLDER_FULL_NAME)
    for i in range(0,len(list)):
        vid_file_name = list[i]
        vid_file_full_name = os.path.join(VID_FOLDER_FULL_NAME, vid_file_name)
        # sys.stdout.write(vid_file_full_name+"\n")

        if vidder.ffmpeg_check(vid_file_full_name):
            vidder.add_thumbnail_to_vid(vid_file_full_name)
        else:
            vidder.re_encode_vid(vid_file_full_name)

        # if os.path.isfile(vid_file_full_name) and convert_vids_to_txt_opencv_paddleocr.is_media_file(vid_file_full_name) and add_thumbnail_to_vid_opencv_ffmpeg.ffmpeg_check(vid_file_full_name):
        #     sys.stdout.write("\n{}\n".format("-"*200))
        #     sys.stdout.write("{:<20}:{}\n\n".format("vid_file_full_name", vid_file_full_name))
        #     add_thumbnail_to_vid_opencv_ffmpeg.add_thumbnail_to_vid(vid_file_full_name)

if __name__ == "__main__":
    main()


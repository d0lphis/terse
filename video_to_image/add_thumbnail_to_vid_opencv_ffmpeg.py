# coding=utf-8

# [requirement]
# pip install opencv-python
# pip install numpy

# [usage]
# python add_thumbnail_to_vid_opencv_ffmpeg.py a.mp4

import sys
import vidder






def main():
    VID_FILE_FULL_NAME = sys.argv[1]

    # res=ffmpeg_check(VID_FILE_FULL_NAME)
    # print(res)
    # sys.exit()

    vidder.add_thumbnail_to_vid(VID_FILE_FULL_NAME)


if __name__ == "__main__":
    main()

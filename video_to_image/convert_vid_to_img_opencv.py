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
import cv2, ffmpeg

import vidder






def main():

    SPLITTER = "-"*80
    sys.stdout.write("\n{}\n".format(SPLITTER))
    # sys.stdout.flush()

    # extract_frequency = 100
    VID_FILE_FULL_NAME = sys.argv[1]
    SELECTION = sys.argv[2]
    destination_folder = os.path.splitext(VID_FILE_FULL_NAME)[0]

    sys.stdout.write("{:<20}:{}\n{:<20}:{}\n{:<20}:{}\n\n".format("VID_FILE_FULL_NAME", VID_FILE_FULL_NAME, "SELECTION", SELECTION, "destination_folder", destination_folder))
    #sys.exit()



    try:
        shutil.rmtree(destination_folder)
    except OSError:
        pass
    os.mkdir(destination_folder)

    # if ffmpeg_check(VID_FILE_FULL_NAME):
    frames = vidder.extract_frames(VID_FILE_FULL_NAME, destination_folder, SELECTION)
    # else:
    #     sys.exit(1)
    # print(frames)

    for index, frame in enumerate(frames):
        save_path = r"{}/{:>03d}.jpg".format(destination_folder, index)
        # cv2.imwrite(save_path, frame)
        cv2.imencode('.jpg', frame)[1].tofile(save_path)
    sys.stdout.write("\n\n" + str(len(frames)) + " frame saved.")



if __name__ == "__main__":
    main()

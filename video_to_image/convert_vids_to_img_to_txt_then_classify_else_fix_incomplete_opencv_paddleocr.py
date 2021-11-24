# coding=utf-8

# [usage]
# python convert_vids_to_img_to_txt_then_classify_else_fix_incomplete_opencv_paddleocr.py video_folder douyin
# python convert_vids_to_img_to_txt_then_classify_else_fix_incomplete_opencv_paddleocr.py video_folder bilibili


import sys, os, shutil

import cv2
import vidder



class HiddenPrints:
    def __init__(self, activated=True):
        # activated参数表示当前修饰类是否被**
        self.activated = activated
        self.original_stdout = None

    def open(self):
        sys.stdout.close()
        sys.stdout = self.original_stdout

    def close(self):
        self.original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __enter__(self):
        if self.activated:
            self.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.activated:
            self.open()








classifications = {}

VID_FOLDER_FULL_NAME = sys.argv[1]
SELECTION = sys.argv[2]
if SELECTION == "douyin":
    SELECTION = "save_last_frame_by_desc_traversing"
elif SELECTION == "bilibili":
    # SELECTION = "20"
    SELECTION = "save_middle_frame_by_desc_traversing"
# elif SELECTION.isnumeric():
#     SELECTION = SELECTION
# print(SELECTION)
# sys.exit()

list = os.listdir(VID_FOLDER_FULL_NAME)
for i in range(0,len(list)):
    vid_file_name = list[i]
    vid_file_full_name = os.path.join(VID_FOLDER_FULL_NAME,vid_file_name)
    extract_folder = os.path.splitext(vid_file_full_name)[0]
    if os.path.isfile(vid_file_full_name) and vidder.is_media_file(vid_file_full_name):
        if vidder.ffmpeg_check(vid_file_full_name):
            # sys.stdout.write("{}\n".format(vid_file_name))
            # os.system('python convert_vid_to_img_opencv.py '+path+' save_last_frame_by_desc_traversing')
            # os.system('python img2txt_paddleocr.py a.jpg')
            # sys.stdout.write("{}\n".format(path))
            sys.stdout.write("\n{}\n".format("-"*200))
            sys.stdout.write("{:<20}:{}\n{:<20}:{}\n{:<20}:{}\n\n".format("vid_file_full_name", vid_file_full_name, "SELECTION", SELECTION, "extract_folder", extract_folder))

            # try:
            #     shutil.rmtree(extract_folder)
            # except OSError:
            #     pass
            # os.mkdir(extract_folder)

            # stdout_ori = sys.stdout
            # f = open(os.devnull, 'w')
            # sys.stdout = f
            

            # if vidder.ffmpeg_check(vid_file_full_name):
            frames = vidder.extract_frames(vid_file_full_name, extract_folder, SELECTION)    #a list with only one element containing vid last frame
            # else:
            #     continue

            for index, frame in enumerate(frames):
                # save_path = "{}/{:>03d}.jpg".format(extract_folder, index)
                # cv2.imwrite(save_path, frame)



                # Myprint= HiddenPrints()
                # Myprint.close()

                texts = vidder.extract_texts(frame)

                # Myprint.open()



                # sys.stdout.write(str(texts))

                user_nick_name = None
                user_id = None
                #douyin watermark usually at last frame
                # if not SELECTION.isnumeric():
                if SELECTION == "save_last_frame_by_desc_traversing":
                    for line in texts:
                        ocr_text = line[1][0]
                        print(ocr_text)
                        if ocr_text.startswith("@"):
                            user_nick_name = ocr_text.replace("@", "").strip().replace(":", "_")
                        elif ocr_text.startswith("抖音号："):
                            user_id = ocr_text.replace("抖音号：", "").strip()
                        # print(line[1][0])
                #bilibili watermark usually at last frame
                else:
                    for line in texts:
                        ocr_text = line[1][0]
                        print(ocr_text)
                        user_nick_name = ocr_text.strip().replace(":", "_")
                        break
                
                classifications[vid_file_name] = user_nick_name if user_nick_name is not None else user_id


            # f.close()
            # sys.stdout = stdout_ori

            sys.stdout.write("\n\n" + str(len(frames)) + " frame saved.")
        else:
            vidder.re_encode_vid(vid_file_full_name)


# sys.exit()


sys.stdout.write("\n\n\n\n\n\n")
# sys.stdout.write(str(classifications))
for k, v in classifications.items():
    sys.stdout.write("{:<60}\t{}\n".format(k, v))
    if v is not None:
        vid_destination_folder = os.path.join(VID_FOLDER_FULL_NAME,v)
        if not os.path.exists(vid_destination_folder):
            try:
                os.makedirs(vid_destination_folder)
            except OSError as e:
                raise
                sys.exit()

        try:
            shutil.move(os.path.join(VID_FOLDER_FULL_NAME,k), vid_destination_folder)
        except:
            continue


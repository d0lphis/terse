

def is_media_file(file_path):
    import mimetypes
    mimetypes.init()

    mimestart = mimetypes.guess_type(file_path)[0]

    if mimestart != None:
        mimestart = mimestart.split('/')[0]

        # if mimestart in ['audio', 'video', 'image']:
        if mimestart in ['video']:
            return True
        else:
            return False

def ffmpeg_check(vid_file_full_name):
    import subprocess

    # res = os.system('ffmpeg -v error -i \"' + vid_file_full_name + '\" -f null - 2>&1')
    out = subprocess.check_output('ffmpeg -v error -i \"' + vid_file_full_name + '\" -f null - 2>&1', shell=True) 
    print(out)
    if str(out).find('partial file') != -1 :
        return False
    else:
        return True

def extract_frames(vid_file_full_name, destination_folder, selection):
    import sys, os, shutil
    import cv2

    frames = []

    video = cv2.VideoCapture()
    if not video.open(vid_file_full_name):
        print("can not open the video")
        exit(1)

    index = 0
    count = 0
    last_frame = None
    frame = None
    while True:
        index += 1
        _, frame = video.read()
        # _, frame = video.retrieve()
        # _, frame = video.grab()
        # save_path = "{}/{:>03d}.jpg".format(destination_folder, index)
        if selection == "save_first_frame":
            frames.append(frame)
            # cv2.imwrite(save_path, frame)
            # sys.stdout.write("First frames saved.")
            break
        elif selection == "save_all_frames":
            if frame is None:
                # sys.stdout.write("\n\nAll frames saved.")
                break
            frames.append(frame)
            # cv2.imwrite(save_path, frame)
            sys.stdout.write("\rFrames traversed 0 -> {:d}.".format(count))
            count += 1
        elif selection == "save_last_frame_by_asc_traversing":
            if frame is None:
                frames.append(frame)
                # cv2.imwrite(save_path, last_frame)
                # sys.stdout.write("\n\nLast frame saved.")
                break
            last_frame = frame
            sys.stdout.write("\rFrames traversed 0 -> {:d}.".format(count))
            count += 1
        elif selection == "save_last_frame_by_desc_traversing" or selection == "save_middle_frame_by_desc_traversing":
            frames_count = current_frame_number = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
            fps = int(video.get(cv2.CAP_PROP_FPS))
            duration = 1000*frames_count/fps
            last = int(video.get(cv2.CAP_PROP_POS_AVI_RATIO))
            # last_timestamp = str(datetime.timedelta(seconds=seconds))
            frame_number = ((frames_count-1)/(duration*fps))
            sys.stdout.write("{:<20}:{}\n{:<20}:{}\n{:<20}:{}\n{:<20}:{}\n{:<20}:{}\n\n".format("FRAMES", frames_count, "FPS", fps, "DURATION", duration, "FRAME_NUMBER", frame_number, "LAST", last))
            # video.set(cv2.CAP_PROP_POS_MSEC, duration)
            while last_frame is None:
                video.set(cv2.CAP_PROP_POS_FRAMES,current_frame_number)
                _, last_frame = video.read()
                sys.stdout.write("\rFrames traversed {:d} -> {:d}.".format(frames_count,current_frame_number))
                current_frame_number = current_frame_number - 1
            
            if selection != "save_middle_frame_by_desc_traversing":
                frames.append(last_frame)
            else:
                video.set(cv2.CAP_PROP_POS_FRAMES,int(current_frame_number/2))
                _, middle_frame = video.read()
                frames.append(middle_frame)

            # cv2.imwrite(save_path, last_frame)
            # sys.stdout.write("\n\nLast frame saved.")
            break
        elif selection.isnumeric():
            video.set(cv2.CAP_PROP_POS_FRAMES,int(selection))
            _, frame = video.read()
            frames.append(frame)
            break



    video.release()
    sys.stdout.write("\n")

    return frames



def extract_texts(img_file_path_or_frame):
    from paddleocr import PaddleOCR,draw_ocr

    # img_file_path = '381.jpg'

    # Paddleocr supports Chinese, English, French, German, Korean and Japanese. You can set the parameter `lang` as `ch`, `en`, `french`, `german`, `korean`, `japan` to switch the language model in order.
    ocr = PaddleOCR(use_angle_cls=True, use_gpu=False, lang='ch', show_log=False, version='PP-OCR') # need to run only once to download and load model into memory
    # texts = ocr.ocr(img_file_path, cls=True)
    texts = ocr.ocr(img_file_path_or_frame, cls=True)

    return texts

    # # draw texts
    # from PIL import Image
    # image = Image.open(IMG_FILE_FULL_NAME).convert('RGB')
    # boxes = [line[0] for line in texts]
    # txts = [line[1][0] for line in texts]
    # scores = [line[1][1] for line in texts]
    # im_show = draw_ocr(image, boxes, txts, scores, font_path='/path/to/PaddleOCR/doc/fonts/simfang.ttf')
    # im_show = Image.fromarray(im_show)
    # im_show.save('texts.jpg')

def add_thumbnail_to_vid(vid_file_full_name):
    import sys, os, shutil, subprocess
    import cv2

    destination_folder = os.path.splitext(vid_file_full_name)[0]
    vid_file_name = os.path.basename(vid_file_full_name)

    SELECTION = "save_first_frame"

    vid_thumbnail_full_name = os.path.join(destination_folder, '000.jpg')
    # vid_parent_folder_full_name = os.path.dirname(vid_file_full_name)
    destination_vid_file_full_name = os.path.join(destination_folder, vid_file_name)

    frames = extract_frames(vid_file_full_name, destination_folder, SELECTION)

    try:
        shutil.rmtree(destination_folder)
    except OSError:
        pass
    os.mkdir(destination_folder)
    for index, frame in enumerate(frames):
        save_path = "{}/{:>03d}.jpg".format(destination_folder, index)
        cv2.imencode('.jpg', frame)[1].tofile(save_path)
    sys.stdout.write("\n\n" + str(len(frames)) + " frame saved.")
    shutil.move(vid_file_full_name, destination_folder)                 #move original vid to same name folder as backup

    #add thumbnail to vid
    out = subprocess.check_output('ffmpeg -i \"' + os.path.join(destination_folder, vid_file_name) + '\" -i \"' + vid_thumbnail_full_name + '\" -map 1 -map 0 -c copy -disposition:0 attached_pic \"' + vid_file_full_name + '\"', shell=True) 
    print(out)

def re_encode_vid(vid_file_full_name):
    import sys, os, shutil, subprocess
    import cv2

    destination_folder = os.path.splitext(vid_file_full_name)[0]
    vid_file_name = os.path.basename(vid_file_full_name)

    os.mkdir(destination_folder)
    shutil.move(vid_file_full_name, destination_folder)                 #move original vid to same name folder as backup

    #re encode to fix incomplete vid
    out = subprocess.check_output('ffmpeg -i \"' + os.path.join(destination_folder, vid_file_name) + '\" -c:v libx264 -preset veryslow -crf 18 -c:a copy \"' + vid_file_full_name + '\"', shell=True) 
    print(out)
from cv2 import putText, imshow, waitKey, VideoCapture, imwrite
from cv2 import CAP_PROP_POS_FRAMES, FONT_HERSHEY_SIMPLEX, LINE_AA, IMWRITE_JPEG_QUALITY
from scenedetect import detect, AdaptiveDetector
from utilities import is_video_file, is_folder, is_full_path, resizing_handler, get_aspect_ratio, progress_bar
import os
import sys

resize_flag = True
resize_check = False

aspect_16_9 = 16 / 9
aspect_4_3 = 4 / 3
resize_x = 0
resize_y = 0

original_file_name = ""

def detect_scenes(file_path, DetectorType = None):
    # Planning to change the detector type through argument flags
    if DetectorType == None:
        DetectorType = AdaptiveDetector()
    
    # Detecting the different scenes
    scenes_list = detect(video_path=file_path, detector=AdaptiveDetector(), show_progress=True)
    return scenes_list

def store_pictures(output_folder_path, file_path, file_name, scenes_list, directory_option=False):

    print(f"Storing {len(scenes_list)} frames from \"{file_name}\", inside \"{output_folder_path}\"")

    # Setting up text variables
    cap = VideoCapture(file_path)
    cap.set(CAP_PROP_POS_FRAMES, scenes_list[0][0].frame_num)
    ret, frame = cap.read()
    y,x = frame.shape[:2]

    # Setup to resize output frames
    if(resize_flag):
        aspect_ratio = get_aspect_ratio(x,y)
        if(aspect_ratio == aspect_16_9 and y > 720):
            resize_x = 1280
            resize_y = 720
            frame = resizing_handler(frame, resize_x, resize_y)
            y,x = frame.shape[:2]
            resize_check = True
        elif(aspect_ratio == aspect_4_3 and y > 720):
            resize_x = 960
            resize_y = 720
            frame = resizing_handler(frame, resize_x, resize_y)
            y,x = frame.shape[:2]
            resize_check = True
        else:
            resize_check = False
    
    # Burned text setup
    if(y == 720):
        tY = y-30
        tX = (x/3) - 40
        time_point = (int(tX), int(tY))
        file_point = (20,30)
        fileFontScale = 1
        timeFontScale = 2.5
        thickness_mult = 2
    else:
        tY = y-10
        tX = x/4
        time_point = (int(tX), int(tY))
        file_point = (20,30)
        fileFontScale = 1
        timeFontScale = 1.5
        thickness_mult = 1

    index = 1
    length = len(scenes_list)

    # Storing frames
    for scene in scenes_list:
        progress = index / length
        progress_bar(progress)
        frame_number = f"{scene[0].frame_num}.jpg"
        file_path = os.path.join(output_folder_path, frame_number)
        cap.set(CAP_PROP_POS_FRAMES, scene[0].frame_num)
        ret, frame = cap.read()

        if(resize_flag and resize_check):
            frame = resizing_handler(frame, resize_x, resize_y)
            y,x = frame.shape[:2]

        # Burn original file name into frame
        putText(img=frame, text=str(file_name), org=file_point, fontFace=FONT_HERSHEY_SIMPLEX, fontScale=fileFontScale, color=(0,0,0), thickness=4 * thickness_mult, lineType=LINE_AA)
        putText(img=frame, text=str(file_name), org=file_point, fontFace=FONT_HERSHEY_SIMPLEX, fontScale=fileFontScale, color=(255,255,255), thickness=2 * thickness_mult, lineType=LINE_AA)

        # Burn timecode into frame
        putText(img=frame, text=str(scene[0].get_timecode()), org=time_point, fontFace=FONT_HERSHEY_SIMPLEX, fontScale=timeFontScale, color=(0,0,0), thickness=4 * thickness_mult, lineType=LINE_AA)
        putText(img=frame, text=str(scene[0].get_timecode()), org=time_point, fontFace=FONT_HERSHEY_SIMPLEX, fontScale=timeFontScale, color=(255, 255, 255), thickness=2 * thickness_mult, lineType=LINE_AA)

        imwrite(file_path, frame, [IMWRITE_JPEG_QUALITY, 50])
        index+=1
    print("\n")
    
    cap.release()
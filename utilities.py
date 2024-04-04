import os
import sys
import time
from cv2 import resize

def get_aspect_ratio(width, height):
    return width/height

def resizing_handler(frame, width, height):
    resized_frame = resize(frame, (width,height))
    return resized_frame

def is_video_file(filename):
    video_suffixes = ['.mp4', '.avi', '.mov', '.mkv', '.webm', '.wmv', '.m4v']
    for suffix in video_suffixes:
        if filename.endswith(suffix):
            return True
    return False

def is_folder(path):
    return os.path.isdir(path)

def is_full_path(path):
    return os.path.sep in path

def progress_bar(progress):
    bar_length = 20
    block = int(round(bar_length * progress))
    text = "\r[{0}] {1:.0f}%".format("#" * block + "-" * (bar_length - block), progress * 100)
    sys.stdout.write(text)
    sys.stdout.flush()

def get_path_details(file_path, main_directory_path):
    if(is_full_path(file_path)):
        original_file_name = os.path.basename(file_path)
        file_name = os.path.splitext(original_file_name)[0]

        directory_path = os.path.dirname(file_path)
        folder_name = f"[Scenes] {file_name}"
        output_folder_path = os.path.join(directory_path, folder_name)

        return output_folder_path, original_file_name
    elif(is_video_file(file_path)):
        original_file_name = os.path.basename(file_path)
        file_name = os.path.splitext(original_file_name)[0]

        folder_name = f"[Scenes] {file_name}"
        output_folder_path = os.path.join(main_directory_path, folder_name)
                  
        return output_folder_path, original_file_name
    else:
        print(f"Path handling error: {file_path}")
        print("Aborting...")
        sys.exit(1)

def format_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours)} hours, {int(minutes)} minutes and {int(seconds)} seconds."
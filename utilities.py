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
import os
import sys
from detect import detect_scenes, store_pictures
from utilities import is_video_file, is_folder, is_full_path

current_path = os.path.dirname(os.path.abspath(__file__))

def main(arguments):
    if "-h" in arguments or "--help" in arguments or len(arguments) == 0:
        print("\nSceneScout written by Sonicfreak, with the usage of scenedetect and opencv.\nThis Python script is utilised to generate preview pictures from video input(s) with the timecode burned into the frames.\nThese pictures get stored in a folder besides the video file.\n\nThe following options are availbe:")
        print("python main.py <video file>")
        print("python main.py <full path to video file>")
        print("python main.py <folder>")
        print("And a mixture of arguments is also accepted, for example:")
        print("python main.py <video file> <path to video file> <path to video file> <folder> <video file>")
        print("\nPlease keep in mind that processing lots of video files and/or video files with a big resolution can take a while.")
    else:
        for argument in arguments:
            # Argument is a video
            if(is_video_file(argument)):
                # A full path to the video has been parsed
                if(is_full_path(argument)):
                    print(f"Scouting {argument}")
                    scene_list = detect_scenes(argument)
                    if(len(scene_list) > 0):
                        store_pictures(argument, current_path, scene_list)
                    else:
                        print(f"WARNING: no scenes detected in {argument}")
                # Just the video title has been parsed
                else:
                    print(f"Scouting {argument}")
                    scene_list = detect_scenes(os.path.join(current_path, argument))
                    if(len(scene_list) > 0):
                        store_pictures(os.path.join(current_path, argument), current_path, scene_list)
                    else:
                        print(f"WARNING: no scenes detected in {argument}")
            # Argument is a folder
            elif(is_folder(argument)):
                for file in os.listdir(argument):
                    file_path = os.path.join(argument, file)
                    # Check if file in the folder is a video file
                    if(is_video_file(file)):
                        print(f"Scouting {file}")
                        scene_list = detect_scenes(file_path)
                        if(len(scene_list) > 0):
                            store_pictures(file_path, argument, scene_list, directory_option=True)
                        else:
                            print(f"WARNING: no scenes detected in {file_path}")
            else:
                print(f"ERROR: could not handle argument: {argument}")

if __name__ == '__main__':
    # Exclude file name from argument list
    arguments = sys.argv[1:]
    main(arguments)
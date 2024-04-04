import os
import sys
import time
from detect import detect_scenes, store_pictures
from utilities import is_video_file, is_folder, is_full_path, get_path_details, format_time

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
        start_time = time.time()
        for argument in arguments:
            # Argument is a video
            if(is_video_file(argument)):

                # A full path to the video has been parsed
                if(is_full_path(argument)):
                    output_folder_path, file_name = get_path_details(argument, current_path)
                    file_path = argument
                    if(os.path.exists(output_folder_path)):
                        print(f"\nNOTE: Scenes folder for \"{argument}\" already exists, skipping this file.")
                        continue
                    print(f"\nScouting {argument}")
                    scenes_list = detect_scenes(argument)
                    if(len(scenes_list) > 0):
                        os.makedirs(output_folder_path)
                        store_pictures(output_folder_path, file_path, file_name, scenes_list)
                    else:
                        print(f"\nWARNING: no scenes detected in {argument}")

                # Just the video title has been parsed
                else:
                    output_folder_path, file_name = get_path_details(argument, current_path)
                    file_path = os.path.join(current_path, argument)
                    if(os.path.exists(output_folder_path)):
                        print(f"\nNOTE: Scenes folder for \"{argument}\" already exists, skipping this file.")
                        continue
                    print(f"\nScouting {argument}")
                    scenes_list = detect_scenes(file_path)
                    if(len(scenes_list) > 0):
                        os.makedirs(output_folder_path)
                        store_pictures(output_folder_path, file_path, file_name, scenes_list)
                    else:
                        print(f"\nWARNING: no scenes detected in {argument}")

            # Argument is a folder
            elif(is_folder(argument)):
                for file in os.listdir(argument):
                    # Check if file in the folder is actually a video file
                    if(is_video_file(file)):
                        file_path = os.path.join(argument, file)
                        output_folder_path, file_name = get_path_details(file_path, current_path)
                        if(os.path.exists(output_folder_path)):
                            print(f"\nNOTE: Scenes folder for \"{file_path}\" already exists, skipping this file.")
                            continue
                        print(f"\nScouting {file}")
                        scenes_list = detect_scenes(file_path)
                        if(len(scenes_list) > 0):
                            os.makedirs(output_folder_path)
                            store_pictures(output_folder_path, file_path, file_name, scenes_list)
                        else:
                            print(f"\nWARNING: no scenes detected in {file_path}")
            else:
                print(f"\nERROR: could not handle argument: {argument}")

        # End of for loop
        end_time = time.time()
        elapsed_time = end_time - start_time
        formatted_time = format_time(elapsed_time)

        print("\n\nDone!")
        print(f"Processing took: {formatted_time}")
        input("Press any key to exit...")

if __name__ == '__main__':
    # Exclude the very first argument (the name of the script)
    arguments = sys.argv[1:]
    main(arguments)
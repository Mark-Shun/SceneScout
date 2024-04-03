# Scene Scout
An utility Python script to generate preview pictures from video files.

## What is this?
Have you ever scrubbed through countless videos on a timeline to find a specific kind of scene to use for your video edit?
This script has been created due to me wanting to automate this process a little bit. Though definitely not perfect it has the ability to go through video content and detect whenever a new scene occurs in the video with the usage of the PySceneDetect module. The script then stores these scenes as small pictures in a seperate folder, in this picture it "burns" the video title and the timecode at which the scene occurs. If all went well you're left with a folder full of images of different scenes you can quickly get an overview of. When finding a scene you might be interested in you can directly navigate to the scene through the timecode burned in the picture.

## Abilities
In essence this script automates the task of detecting scenes and storing said scenes as pictures in a new folder.
The interesting part is that you can parse different input material at once
- A video file
- A path to a video
- A folder with video files (the script does not go deeper into the folders of the parsed folder, just the files in the root of the folder.)
- A mixture of the inputs above

  Due to this you are able to give the script lots of media to process and let it do its thing in the background.

## Setup
### Prerequisites
- [Python](https://www.python.org/)
- [scenedetect](https://www.scenedetect.com/) (can get it through pip)
- [opencv](https://opencv.org/) (more specifically opencv-python)

## Running
Get the latest release or directly clone the repository
```bash
git clone https://github.com/Mark-Shun/SceneScout.git
```

Navigate to your directory and install the dependencies manually or through the requirements.txt
```bash
cd SceneScout
pip install -r requirements.txt
```

Now you can use the script by directly drag and dropping the file(s)/folder(s) into the main.py file in your file explorer.
Or you can enter the argument(s) manually in your command shell, for example:
```bash
python main.py video.mp4 "c:/path/to/video/video.mkv" "c:/path/to/folder/with/videos"
```

##
# Produce-video
This repository details how to generate a video from spatial data. The video is generated via the following steps:

- The data is generated from the *Wave_Propagation.cpp* file. This produces a series of *dat* files that are stored in the *data* folder. 
- Each individual *dat* file is then converted into a graph using the script *produceFrames.py* and stored in the *images* folder. 
- The images are then converted into a video using the script *produceVideo.py*, as shown below.

![alt-text](Wave_Propagation_Video(GIF).gif)

## How to use this code

Cloning this repository will give the user access to all of the above code. For a user who already has spatial data, and would like to
convert this data into a similar video, they can do so by following these steps:

- After having cloned the repository, go into the *data* folder and delete all of the *dat* files there. Then, replace the deleted files with the relevant files.
- Go into the images folder and delete all of the files.
- Run the following command in the terminal to ensure all the relevant packages are correctly installed  
```
pip install -r requirements.txt
```
- Now run the following commands to build the images and produce the video
```
python .\produceFrames.py
python .\produceVideo.py
```
**Note: These are general instructions. The user will likely need to make some minor changes to the python scripts to accommodate for these differences
(e.g. the files containing the data will likely have different names to those given in the repository, and so the code will need to be amended accordingly).**

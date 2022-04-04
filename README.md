# Produce-video
This repository details how to generate a video from spatial data. The video is generated via the following steps:

- The data is generated from the *Wave_Propagation.cpp* file. This produces a series of *dat* files that are stored in the *data* folder. 
- Each individual *dat* file is then converted into a graph using the script *produceFrames.py* and stored in the *images* folder. 
- The images are then converted into a video using the script *produceVideo.py*, as shown below.

![alt-text](Wave_Propagation_Video(GIF).gif)

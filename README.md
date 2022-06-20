# Prerequisites:
1. node 12.16.2
2. Tensorflow
3. Keras
4. Posenet
5. Python 3.8

# Project Objective
Capturing a video and signaling ASL alphabet signs and recognize and display correct alphabet sign classes.

# Steps to run the code
1. Install the prerequisites
2. Run main.py file which gives 3 options 1)Extracting and predicting alphabet videos 2) Extract and predict word videos 3) Predicting alphabets and words.

# Project Implementation
* Record alphabet and word training videos
* Extract video frames for each video 
* Generate keypoints for extracted video frames using posenet
* Based on keypoints extracted crop hand frames based on the position of the wrists
* Use segmentation algorithm to divide each alphabet from the words frames generated based on the x and y coordinates of the left arm, right arm key points generated.
* Combine the segmented frames and predict alphabets and words.

# Links for dataset
* https://drive.google.com/drive/folders/1Rs6GKdX8tpFFY0fjJWbbHyszQ6Qz4bOB?usp=sharing

# Demo Videos
* https://www.youtube.com/watch?v=br4QL6PSxXg&t=342s












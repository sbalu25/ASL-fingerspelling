import glob
import sys

import cv2
import numpy as np
import os
import tensorflow as tf
from handshape_feature_extractor import HandShapeFeatureExtractor
import torch


def get_inference_vector_one_frame_alphabet(files_list):

    model = HandShapeFeatureExtractor.get_instance()
    vectors = []
    video_names = []
    step = int(len(files_list) / 100)
    if step == 0:
        step = 1

    count = 0
    for video_frame in files_list:
        avg_value = []
        img = cv2.imread(video_frame)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        flipped_image = cv2.flip(img, -1)
        avg_value.append(model.extract_feature(img)[0])
        avg_value.append(model.extract_feature(flipped_image)[0])
        total_value = sum(avg_value)/len(avg_value)
        results = total_value
        # results = model.extract_feature(img)
        results = np.squeeze(results)
        predicted = np.where(results==max(results))[0][0]

        vectors.append(predicted)
        video_names.append(os.path.basename(video_frame))

        count += 1
        if count % step == 0:
            # sys.stdout.write("-")
            print("Extracting frame", count)
            sys.stdout.flush()

    return vectors

def load_labels(label_file):
    label = []
    proto_as_ascii_lines = tf.io.gfile.GFile(label_file).readlines()
    for l in proto_as_ascii_lines:
        label.append(l.rstrip())
    return label

def load_label_dicts(label_file):
    id_to_labels = load_labels(label_file)
    labels_to_id = {}
    i = 0

    for id in id_to_labels:
        labels_to_id[id] = i
        i += 1

    return id_to_labels, labels_to_id


def predict_labels_from_frames(video_folder_path):
    files = []
    # wildcard to select all frames for given video file
    path = os.path.join(video_folder_path, "*.png")
    frames = glob.glob(path)
    print("\fframes " + str(len(frames)));
    # sort image frames
    frames.sort()
    files = frames
    prediction_vector = get_inference_vector_one_frame_alphabet(files)
    label_file = 'output_labels_alphabet.txt'
    id_to_labels, labels_to_id = load_label_dicts(label_file)
    final_predictions=[]
    for i in range(len(prediction_vector)):
        for ins in labels_to_id:
            if prediction_vector[i] == labels_to_id[ins]:
                final_predictions.append(ins)
    return final_predictions

def predict_words_from_frames(video_folder_path, start,till):
    files=[]
    for i in range(start,till+1,1):
        try:
            path = os.path.join(video_folder_path, str(i)+".png")
            frames = glob.glob(path)
            files.append(frames[0])
        except:
            continue
    prediction_vector = get_inference_vector_one_frame_alphabet(files)
    label_file = 'output_labels_alphabet.txt'


    id_to_labels, labels_to_id = load_label_dicts(label_file)

    final_predictions=[]
    for i in range(len(prediction_vector)):
        for ins in labels_to_id:
            if prediction_vector[i] == labels_to_id[ins]:
                final_predictions.append(ins)
    return final_predictions

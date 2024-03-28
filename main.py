from ultralytics import YOLO
import cv2


#load models
model = YOLO('yolov8n.yaml')

#use the model
results= model.train(data="config.yaml", epochs=1)  #train the model

# load video

# read frames

# detect vehicles

# track vehicles

# detect license plates

# assign license plate to car

# crop license plate

# process license plate

# read license plate number

# write results
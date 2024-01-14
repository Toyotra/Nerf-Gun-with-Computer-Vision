import pygame
import sys
import cv2 as cv
import imutils
import supervision
import pyfirmata
from ultralytics import YOLO

def cvimage_to_pygame(image): 
    image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
   
    a =  pygame.surfarray.make_surface(image_rgb)
    a = pygame.transform.scale(a, (int(round(a.get_width())), int(round(a.get_height()))))
    a = pygame.transform.flip(a, False, True) 
    return pygame.transform.rotate(a, -90)

def CVInitialize(): 
    cap = cv.VideoCapture(0)

    box = supervision.BoxCornerAnnotator(
            color = supervision.Color.from_hex("#D3EC1A"),
            thickness = 3,
            corner_length = 15

        )
    
    return [cap, box]

def CVWebcapture(cap, box, model):
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=430, height = 200)

    #frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    results = model(source = frame, show = False, conf = 0.55, save = True)[0]
    detections = supervision.Detections.from_ultralytics(results)

    frame = box.annotate(scene = frame, detections = detections)


    return [cv.copyMakeBorder(src=frame, top=10, bottom=10, left=10, right=10, borderType=cv.BORDER_CONSTANT, value=[70, 70, 70]), box.xyxy]
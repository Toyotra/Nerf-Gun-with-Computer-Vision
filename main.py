import pygame
import sys
import cv2 as cv
import imutils
import supervision
import torch
import modelCV
import essentials
import time
import ArduinoCode
from ultralytics import YOLO
from pyfirmata import Arduino, SERVO

wtf = ArduinoCode.idk_what_to_call_this()

#this is in pixels lol
accuracy = 30

torch.cuda.device(1)

Location = [215, 100]
speed = 5
currAngle = 180

pygame.init()
screen = pygame.display.set_mode((1000, 650))
pygame.display.set_caption('AutoAiming Nerf Gun')

pygame.display.set_icon(pygame.image.load("assets/Software logo.png"))


def lock_on():
    if Location[0] > 215 + accuracy:
        currAngle = wtf.servoRotate(True, 9, currAngle)
        return
    elif Location[0] < 215 - accuracy: 
        currAngle = wtf.servoRotate(False, 9, currAngle)
        return
    if Location[1] > 100 + accuracy:
        currAngle = wtf.servoRotate(True, 10, currAngle)
        return
    elif Location[1] < 100 - accuracy: 
        currAngle = wtf.servoRotate(False, 10, currAngle)
        return
    return True


def main():

    mouseHold = False

    model = YOLO("assets/yolov8n-face.pt")
    cap_box = modelCV.CVInitialize()




    background = pygame.image.load("assets/background.png").convert()
    
    if lock_on() != None:
        wtf.servoLock(1, 180)

    while True: #main pygame GUI 
        a = time.time()
        b = modelCV.CVWebcapture(cap_box[0], cap_box[1], model)
        Location = [(b[1].numpy()[0][0] + b[1].numpy()[0][1])/2, (b[1].numpy()[1][0]/ + b[1].numpy()[1][1])/2]

        
        frame = modelCV.cvimage_to_pygame(b[0])

        mx, my = pygame.mouse.get_pos()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

                

        screen.blit(background, (0,0))
        screen.blit(frame, (400, 50))



        #a = essentials.buttonValIncrease(but1, but2, [mx, my], [100, 100], screen, mouseHold)

        pygame.display.flip()

        print(time.time() - a )



if __name__ == "__main__":
    main()
        
        

        
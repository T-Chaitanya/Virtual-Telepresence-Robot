import RPi.GPIO as GPIO



#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)


def forward():
    GPIO.output(7,False)
    GPIO.output(11,True)
    GPIO.output(13,False)
    GPIO.output(15,True)
def backward():
    GPIO.output(7,True)
    GPIO.output(11,False)
    GPIO.output(13,True)
    GPIO.output(15,False)
def right():
    GPIO.output(7,True)
    GPIO.output(11,False)
    GPIO.output(13,False)
    GPIO.output(15,True)
def left():
    GPIO.output(7,False)
    GPIO.output(11,True)
    GPIO.output(13,True)
    GPIO.output(15,False)
def stop():
    GPIO.output(7,False)
    GPIO.output(11,False)
    GPIO.output(13,False)
    GPIO.output(15,False)


import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Car Control')
pygame.mouse.set_visible(1)


while True:
    #print ("doing a function")
    for event in pygame.event.get():
        
        if (event.type == KEYUP):
            print ("key released")
            stop()
        elif  (event.type == KEYDOWN):
            x = pygame.key.name(event.key)
            print((x))
            if x == 'up':
                forward()
            elif x == "down":
                backward()
            elif x == "left":
                left()
            elif x == "right":
                right()

    

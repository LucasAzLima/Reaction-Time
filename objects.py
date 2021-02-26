import cv2
import random

def circleList():
    class addCircle:
        def __init__(self, color, name, key):
            self.color = color
            self.name = name
            self.key = key

    list = []
    list.append(addCircle((0, 0, 255), 'red', 'q'))
    list.append(addCircle((255, 0, 0), 'blue', 'w'))
    list.append(addCircle((0, 255, 0), 'green', 'e'))
    list.append(addCircle((0, 255, 255), 'yellow', 'r'))
    return list


class circles:
    posX = random.randrange(50, 590)
    posY = random.randrange(50, 430)
    color = (255, 0, 0)
    key = 'w'
    time = []
    score = 10

    def position(self):
        return(self.posX, self.posY)

    def Avarage(self):
        soma = 0.0
        for t in self.time:
            soma += t
        return "{:.5f}".format(soma/10.0)


def newCircle(img, key, t1, t2, circle, list):
    img = cv2.circle(img, circle.position(), 50, (0, 0, 0), -1)
    if(ord(key) != ord(circle.key)):
        circle.score -= 1
    rndCircle = random.randrange(0, 4)
    while(ord(circle.key) == ord(list[rndCircle].key)):
        rndCircle = random.randrange(0, 4)
    circle.color = list[rndCircle].color
    circle.key = list[rndCircle].key
    circle.posX = random.randrange(50, 590)
    circle.posY = random.randrange(50, 430)
    circle.time.append(t2-t1)
    return circle
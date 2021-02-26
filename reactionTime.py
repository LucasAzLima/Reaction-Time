import cv2
import numpy as np
import random
import time

#modules
import menu
import objects

empty = np.zeros((480, 750, 3), dtype=np.float32)
empty = menu.menu(empty)
empty2 = empty.copy()

list = objects.circleList()

circle = objects.circles()
rodada = 0
time1 = 0

cv2.namedWindow("Reaction time")
start = False


while(True):
    if start and rodada<10:
        empty = cv2.circle(empty, circle.position(), 50, circle.color, -1)
    elif rodada<10 and not start:
        empty = menu.start(empty)

    cv2.imshow('Reaction time', empty)

    key = cv2.waitKey(30) & 0xff
    if key == ord('x'):
        break
    elif key == ord('q') and rodada<10:
        circle = objects.newCircle(empty, 'q', time1, time.time(), circle, list)
        rodada += 1
        time1 = time.time()

    elif key == ord('w') and rodada<10:
        circle = objects.newCircle(empty, 'w', time1, time.time(), circle, list)
        rodada += 1
        time1 = time.time()

    elif key == ord('e') and rodada<10:
        circle = objects.newCircle(empty, 'e', time1, time.time(), circle, list)
        rodada += 1
        time1 = time.time()

    elif key == ord('r') and rodada<10:
        circle = objects.newCircle(empty, 'r', time1, time.time(), circle, list)
        rodada += 1
        time1 = time.time()

    elif key == ord('s') and rodada<10:
        empty = empty2.copy()
        start = True
        time1 = time.time()

    elif key == ord('d'):
        start = False
        time1 = 0
        rodada = 0
        empty = empty2.copy()
        circle.posX = random.randrange(50, 590)
        circle.posY = random.randrange(50, 430)
        circle.color = (255, 0, 0)
        circle.key = 'w'
        circle.time = []
        circle.score = 10
        
    elif rodada >= 10:
        empty = empty2.copy()
        empty = menu.score(empty, circle.score, circle.Avarage())
        
import cv2
import numpy as np


def menu(img):
    img = cv2.line(img, (640, 0), (640, 480), (255, 255, 255), 1)
    img = cv2.putText(img, 'Q = RED', (645, 28), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 0, 255), 1, cv2.LINE_4)
    img = cv2.putText(img, 'W = BLUE', (645, 116), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (255, 0, 0), 1, cv2.LINE_4)
    img = cv2.putText(img, 'E = GREEN', (645, 204), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 255, 0), 1, cv2.LINE_4)
    img = cv2.putText(img, 'R = YELLOW', (645, 292), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 255, 255), 1, cv2.LINE_4)
    img = cv2.putText(img, 'X = QUIT', (645, 380), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (255, 0, 255), 1, cv2.LINE_4)
    img = cv2.putText(img, 'D = RESET', (645, 460), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (100, 1, 255), 1, cv2.LINE_4)
    return img


def score(img, score, avarage):
    img = cv2.putText(img, 'Your score: ' + str(score), (50, 240), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 255, 0), 2, cv2.LINE_AA)
    img = cv2.putText(img, 'Average time: ' + avarage, (50, 270), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 255, 0), 2, cv2.LINE_AA)
    return img


def start(img):
    img = cv2.putText(img, 'Press "s" to start', (50, 240), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (255, 0, 0), 2, cv2.LINE_AA)
    return img

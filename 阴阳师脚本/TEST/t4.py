import cv2
from PIL import ImageGrab
import pyautogui as pag

if __name__ == '__main__':
    image = ImageGrab.grab(bbox=(250, 140, 1670, 940))
    image.save("img/1.png", "PNG")
    image = cv2.imread("img/1.png", 0)
    btn_image = cv2.imread("img/tansuo.png", 0)

    res = cv2.matchTemplate(btn_image, image, cv2.TM_CCOEFF_NORMED)
    if res.max() > 0.7:
        pag.click(1038, 307)

import cv2
from PIL import Image
from PIL import ImageStat
from PIL import ImageEnhance


def delta_brightness(source_texture, overlayed_texture):
    return ImageStat.Stat(Image.open(overlayed_texture).convert('L')).mean[0]-ImageStat.Stat(Image.open(source_texture).convert('L')).mean[0]

def adjust_saturation(img, saturation_factor):
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(saturation_factor)
    return img

def change_brightness(imgpath, value=30):
    img = cv2.imread(imgpath)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v,value)
    v[v > 255] = 255
    v[v < 0] = 0
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img


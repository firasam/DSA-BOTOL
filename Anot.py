import os
import cv2
import lxml.etree as etree
import xml.etree.cElementTree as ET


def write_xml(folder, img, objects, tl, br, savedir):
    if not os.path.isdir(savedir):
        os.mkdir(savedir) 
    image = cv2.imread(img.path)
    height, width, depth = image.shape
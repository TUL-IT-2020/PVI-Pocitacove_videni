import os
import numpy as np
import cv2

def find(folder, file_type: str = ["jpg"]):
    cwd = os.getcwd()
    folder = os.path.join(cwd, folder)
    picture_files = []
    print("Current working directory: {0}, files: ".format(cwd))
    for file in os.listdir(folder):
        # TODO: get file format
        print(file)
        picture_files.append(os.path.join(folder, file))
    return picture_files


def load(picture_files: list[str]) -> list[np.ndarray]:
    """ Load images from files
    get:
        picture_files - list of files
    return:
        images - list of images
    """
    images = []
    for file in picture_files:
        bgr = cv2.imread(file)
        rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
        images.append(rgb)
    return images
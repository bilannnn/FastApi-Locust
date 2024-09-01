import logging

from PIL import Image
import os
import requests

current_dir = os.getcwd()
os.chdir(current_dir + "/../")


def dir_check(dir_location):
    exist = os.path.exists(dir_location)
    if not exist:
        os.makedirs(dir_location)


def load_image(img_url):
    try:
        img = Image.open(requests.get(img_url, stream=True).raw)
        return img
    except Exception as e:
        logging.error(f"{e}")

import cv2
import numpy as np
import requests
import matplotlib.pyplot as plt


def load_image(url):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        image_array = np.asarray(bytearray(response.raw.read()), dtype=np.uint8)
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        print("Image from URL loaded successfully!")
        return image
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the image: {e}")
        return None


def show_image(title, image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.title(title)
    plt.axis("off")
    plt.show()


def show_gray_channel(title, channel):
    plt.imshow(channel, cmap="gray")
    plt.title(title)
    plt.axis("off")
    plt.show()

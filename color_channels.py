import cv2
import numpy as np
from utils import load_image, show_image, show_gray_channel


print("--- Running Exercise 4: Color Channels ---")

image_url = "https://images.pexels.com/photos/1059905/pexels-photo-1059905.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
original = load_image(image_url)

if original is not None:
    B, G, R = cv2.split(original)

    print("\n--- Splitting Channels ---")
    print("The following images are intensity maps in grayscale.")
    print("Bright areas indicate high intensity of that specific color.")

    show_gray_channel("Blue Channel (B)", B)
    show_gray_channel("Green Channel (G)", G)
    show_gray_channel("Red Channel (R)", R)

    print("\n--- Merging Channels ---")

    zeros = np.zeros(original.shape[:2], dtype="uint8")

    show_image("Blue Channel Only", cv2.merge([B, zeros, zeros]))
    show_image("Green Channel Only", cv2.merge([zeros, G, zeros]))
    show_image("Red Channel Only", cv2.merge([zeros, zeros, R]))

    recomposed_image = cv2.merge([B, G, R])
    show_image("Recomposed Image (Merge of B, G, R)", recomposed_image)
    print(
        "\nUsing merge(), we combine the channels back together to form the original image."
    )

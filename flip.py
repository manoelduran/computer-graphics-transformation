import cv2
from utils import load_image_from_web, show_image


print("--- Exercise 2: Flip (Mirroring) ---")

image_url = "https://images.pexels.com/photos/1059905/pexels-photo-1059905.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
original = load_image_from_web(image_url)

if original is not None:
    show_image("Original", original)

    horizontal_flip = cv2.flip(original, 1)
    show_image("Horizontal Flip (Left to Right)", horizontal_flip)

    vertical_flip = cv2.flip(original, 0)
    show_image("Vertical Flip (Top to Bottom)", vertical_flip)

    print(
        "\nThe flip() function mirrors the image. The code '1' flips horizontally and '0' flips vertically."
    )

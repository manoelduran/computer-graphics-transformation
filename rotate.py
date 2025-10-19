import cv2
from utils import load_image_from_web, show_image

print("--- Running Exercise 3: Rotate ---")

image_url = "https://images.pexels.com/photos/1059905/pexels-photo-1059905.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
original = load_image_from_web(image_url)

if original is not None:
    show_image("Original", original)

    rot_90 = cv2.rotate(original, cv2.ROTATE_90_CLOCKWISE)
    show_image("Rotation 90° Clockwise", rot_90)

    rot_180 = cv2.rotate(original, cv2.ROTATE_180)
    show_image("Rotation 180°", rot_180)

    print("\nThe rotate() function rotates the image in multiples of 90 degrees.")
    print("\nAnswer -> What is the difference between flip and rotate?")
    print(
        " - flip: Reflects the image like a mirror. The image content doesn’t change orientation (the sky remains at the top)."
    )
    print(
        " - rotate: Physically rotates the image. The content changes orientation (after a 90° rotation, the sky is sideways)."
    )

import cv2
from utils import load_image, show_image


print("--- Running Exercise 1: Resizing ---")


image_url = "https://images.pexels.com/photos/1059905/pexels-photo-1059905.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"

original = load_image(image_url)

if original is not None:
    show_image("Original", original)

    small_dim = (60, 40)
    small = cv2.resize(original, small_dim, interpolation=cv2.INTER_AREA)

    large_dim = (600, 400)

    nearest = cv2.resize(small, large_dim, interpolation=cv2.INTER_NEAREST)
    linear = cv2.resize(small, large_dim, interpolation=cv2.INTER_LINEAR)
    cubic = cv2.resize(small, large_dim, interpolation=cv2.INTER_CUBIC)

    show_image("Resized - NEAREST (Pixelated)", nearest)
    show_image("Resized - LINEAR (Smooth/Default)", linear)
    show_image("Resized - CUBIC (Sharper)", cubic)

    print("\nObserve the three resized images:")
    print(" - NEAREST: Fast, but creates a visible blocky (pixelated) effect.")
    print(" - LINEAR: Smooth, a good balance between speed and quality.")
    print(" - CUBIC: Slower, but produces the sharpest and highest-quality result.")
    print(
        "\nAnswer -> Which is the best interpolation method? "
        "For photos, CUBIC is usually the best because it preserves more details."
    )

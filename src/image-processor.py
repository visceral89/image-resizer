from PIL import Image, ImageSequence
import os


def resize_image(image_path, output_size):
    with Image.open(image_path) as img:
        return img.resize(output_size, Image.LANCZOS)


def resize_gif(image_path, output_size):
    with Image.open(image_path) as img:
        frames = [
            frame.convert("RGBA").resize(output_size, Image.LANCZOS)
            for frame in ImageSequence.Iterator(img)
        ]
    return frames


def save_images(image, output_path):
    if isinstance(image, list):
        image[0].save(output_path, save_all=True, append_images=image[1:], loop=1)
    else:
        image.save(output_path)


def process_images(folder_path, output_sizes):
    output_folder = os.path.join(folder_path, "resized")
    os.makedirs(output_folder, exist_ok=True)

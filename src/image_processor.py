from PIL import Image, ImageSequence
import os
from config import EXTENTIONS


def resize_image(image_path, output_size):
    with Image.open(image_path) as img:
        return img.resize(output_size)


def resize_gif(image_path, output_size):
    with Image.open(image_path) as img:
        frames = [
            frame.convert("RGBA").resize(output_size)
            for frame in ImageSequence.Iterator(img)
        ]
    return frames


def save_images(image, output_path):
    if isinstance(image, list):
        image[0].save(
            output_path,
            save_all=True,
            append_images=image[1:],
            loop=0,
        )
    else:
        image.save(output_path)


def process_images(folder_path, output_sizes):
    output_folder = os.path.join(folder_path, "resized")
    os.makedirs(output_folder, exist_ok=True)

    for file in os.listdir(folder_path):
        file_name, file_ext = os.path.splitext(file)
        if file_ext.lower() in EXTENTIONS:
            image_path = os.path.join(folder_path, file)

            for size in output_sizes:
                output_path = os.path.join(
                    output_folder, f"{file_name}@{size}px{file_ext}"
                )
                if file_ext.lower() == ".gif":
                    frames = resize_gif(image_path, (size, size))
                    save_images(frames, output_path)
                else:
                    resized_img = resize_image(image_path, (size, size))
                    save_images(resized_img, output_path)
    os.startfile(output_folder)

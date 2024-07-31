from PIL import Image, ImageSequence


def resize_image(image_path, output_size):
    with Image.open(image_path) as img:
        resized_img = img.resize(output_size)
        return resize_image


def resize_gif(image_path, output_size):
    with Image.open(image_path) as img:
        frames = []

        for frame in ImageSequence.Iterator(img):
            frame = frame.convert("RGBA")
            resized_frame = frame.resize(output_size)
            frames.append(resized_frame)
    return resized_frame

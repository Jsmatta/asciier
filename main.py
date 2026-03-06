from PIL import Image, ImageOps

# More detailed gradient of characters, from darkest to lightest.
ASCII_CHARS = list("█$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^'. ")


def main(new_width=1000):
    path = input("Enter a valid pathname to an image:\n")
    try:
        image = Image.open(path)
    except Exception:
        print(path, " is not a valid pathname to an image.")
        return

    # Convert to grayscale and enhance contrast for more detail.
    img = ImageOps.grayscale(image)
    img = ImageOps.autocontrast(img)

    # Adjust for character aspect ratio (chars are usually taller than wide).
    aspect_ratio = 0.55
    new_height = int(new_width * image.size[1] / image.size[0] * aspect_ratio)
    img = img.resize((new_width, new_height))

    def pixel_to_char(pixel: int) -> str:
        idx = pixel * (len(ASCII_CHARS) - 1) // 255
        return ASCII_CHARS[idx]

    chars = "".join(pixel_to_char(p) for p in img.get_flattened_data())
    ascii_image = "\n".join([chars[i:i+new_width] for i in range(0, len(chars), new_width)])

    open("ascii_image.txt", "w").write(ascii_image)


if __name__ == "__main__":
    main()

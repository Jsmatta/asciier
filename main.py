from PIL import Image

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def main(new_width=100):
    path = input("Enter a valid pathname to an image:\n")
    try:
        image = Image.open(path)
    except:
        print(path, " is not a valid pathname to an image.")
        return

    img = image.resize((new_width, int(new_width * image.size[1]/image.size[0]))).convert("L")
    chars = "".join([ASCII_CHARS[p//25] for p in img.getdata()])
    ascii_image = "\n".join([chars[i:i+new_width] for i in range(0, len(chars), new_width)])
    
    print(ascii_image)
    open("ascii_image.txt", "w").write(ascii_image)

main()

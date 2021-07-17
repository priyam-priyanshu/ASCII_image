from PIL import Image

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# resize Image
def resize_img(image, new_width):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized_img = image.resize((new_width, new_height))
    return resized_img

# Convert into greyscale
def graify(image):
    grey_img = image.convert("L")
    return grey_img

# Pixel to ascii
def pixel_2_ascii(image):

    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters

# main
def main():
    new_width = int(input("Enter required width of image: "))

    path = input("Enter image path: ")
    try:
        img = Image.open(path)
    except:
        print("Invalid image path")

    new_img = pixel_2_ascii(graify(resize_img(img,new_width)))

    # Allign Image
    pixel_count = len(new_img)
    ascii_image = "\n".join([new_img[index:(index+new_width)] for index in range(0, pixel_count, new_width)])

    print(ascii_image)
# call main

main()
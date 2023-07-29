from text_on_image import *

try:
    pos_x = int(input("Input position on x: "))
    pos_y = int(input("input position on y: "))
    font_size = int(input("Input font size: "))
    color_r = int(input("Input value of red color (max 255): "))
    color_g = int(input("Input value of green color (max 255): "))
    color_b = int(input("Input value of blue color (max 255): "))

    text_on_image(pos_x, pos_y, font_size, color_r, color_g, color_b)
except ValueError:
    print("Wrong input, close...")

# input("Enter to close program.") # if needed
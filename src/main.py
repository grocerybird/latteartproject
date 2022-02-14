from PIL import Image
import numpy as np

# Color Assignment
bk = (0, 0, 139)  # Background
cp = (0, 0, 0)  # Cup
cf = (111, 78, 55)  # Coffee
mk = (255, 255, 255)  # Milk

# Latte Prompt
print("Which kind of latte art would you like?")
print("Heart or rosetta?")

while True:
    inp = input()

    if inp == "Heart" or inp == "heart":

        pixels_list_heart = [
            [bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk],
            [bk, bk, bk, bk, bk, bk, bk, bk, bk, cp, cp, cp, cp, cp, cp, cp, bk, bk, bk, bk, bk, bk, bk, bk, bk],
            [bk, bk, bk, bk, bk, bk, bk, bk, cp, cp, cf, cf, cf, cf, cf, cp, cp, bk, bk, bk, bk, bk, bk, bk, bk],
            [bk, bk, bk, bk, bk, bk, bk, cp, cp, cf, cf, cf, cf, cf, cf, cf, cp, cp, bk, bk, bk, bk, bk, bk, bk],
            [bk, bk, bk, bk, bk, bk, cp, cp, cf, cf, cf, cf, cf, cf, cf, cf, cf, cp, cp, bk, bk, bk, bk, bk, bk],
            [bk, bk, bk, bk, bk, cp, cp, cf, cf, cf, cf, cf, cf, cf, cf, cf, cf, cf, cp, cp, bk, bk, bk, bk, bk],
            [bk, bk, bk, bk, cp, cp, cf, cf, cf, cf, cf, cf, cf, cf, cf, cf, cf, cf, cf, cp, cp, bk, bk, bk, bk],
            [bk, bk, bk, bk, cp, cf, cf, cf, cf, cf, cf, cf, cf, cf, cf, cf, cf, cf, cf, cf, cp, cp, bk, bk, bk],
            [bk, bk, bk, cp, cf, cf, cf, cf, cf, mk, mk, cf, cf, cf, mk, mk, cf, cf, cf, cf, cf, cp, cp, cp, cp],
            [bk, bk, bk, cp, cf, cf, cf, cf, mk, mk, mk, mk, cf, mk, mk, mk, mk, cf, cf, cf, cf, cp, bk, bk, cp],
            [bk, bk, bk, cp, cf, cf, cf, mk, mk, mk, mk, mk, mk, mk, mk, mk, mk, mk, cf, cf, cf, cp, bk, bk, cp],
            [bk, bk, bk, cp, cf, cf, cf, mk, mk, mk, mk, mk, mk, mk, mk, mk, mk, mk, cf, cf, cf, cp, bk, bk, cp],
            [bk, bk, bk, cp, cf, cf, cf, mk, mk, mk, mk, mk, mk, mk, mk, mk, mk, mk, cf, cf, cf, cp, bk, bk, cp],
            [bk, bk, bk, cp, cf, cf, cf, mk, mk, mk, mk, mk, mk, mk, mk, mk, mk, mk, cf, cf, cf, cp, bk, bk, cp],
            [bk, bk, bk, cp, cf, cf, cf, mk, mk, mk, mk, mk, mk, mk, mk, mk, mk, mk, cf, cf, cf, cp, bk, bk, cp],
            [bk, bk, bk, cp, cf, cf, cf, mk, mk, mk, mk, mk, mk, mk, mk, mk, mk, mk, cf, cf, cf, cp, bk, bk, cp],
            [bk, bk, bk, cp, cf, cf, cf, mk, mk, mk, mk, mk, mk, mk, mk, mk, mk, mk, cf, cf, cf, cp, cp, cp, cp],
            [bk, bk, bk, cp, cp, cf, cf, cf, mk, mk, mk, mk, mk, mk, mk, mk, mk, cf, cf, cf, cp, cp, bk, bk, bk],
            [bk, bk, bk, cp, cp, cp, cf, cf, cf, mk, mk, mk, mk, mk, mk, mk, cf, cf, cf, cp, cp, cp, bk, bk, bk],
            [bk, bk, bk, cp, cp, cp, cp, cf, cf, cf, mk, mk, mk, mk, mk, cf, cf, cf, cp, cp, cp, cp, bk, bk, bk],
            [bk, bk, bk, cp, cp, cp, cp, cp, cf, cf, cf, mk, mk, mk, cf, cf, cf, cp, cp, cp, cp, cp, bk, bk, bk],
            [bk, bk, bk, cp, cp, cp, cp, cp, cp, cf, cf, cf, cf, cf, cf, cf, cp, cp, cp, cp, cp, cp, bk, bk, bk],
            [bk, bk, bk, cp, cp, cp, cp, cp, cp, cp, cf, cf, cf, cf, cf, cp, cp, cp, cp, cp, cp, cp, bk, bk, bk],
            [bk, bk, bk, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, bk, bk, bk],
            [bk, bk, bk, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, bk, bk, bk],
        ]

        coffee_array = np.array(pixels_list_heart, dtype=np.uint8)
        coffee_image = Image.fromarray(coffee_array)
        coffee_image = coffee_image.resize((480, 480), resample=Image.NEAREST)
        coffee_image.save("coffee_heart.png")

        coffee_heart = Image.open("coffee_heart.png")
        coffee_heart.show()
        print("Thank you")
        break

    if inp == "Rosetta" or inp == "rosetta":

        pixels_list_rosetta = [
            [bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk],
            [bk, bk, bk, bk, bk, bk, bk, bk, bk, cp, cp, cp, cp, cp, cp, cp, bk, bk, bk, bk, bk, bk, bk, bk, bk],
            [bk, bk, bk, bk, bk, bk, bk, bk, cp, cp, cf, cf, cf, cf, cf, cp, cp, bk, bk, bk, bk, bk, bk, bk, bk],
            [bk, bk, bk, bk, bk, bk, bk, cp, cp, cf, cf, cf, cf, cf, cf, cf, cp, cp, bk, bk, bk, bk, bk, bk, bk],
            [bk, bk, bk, bk, bk, bk, cp, cp, cf, cf, cf, cf, cf, cf, cf, cf, cf, cp, cp, bk, bk, bk, bk, bk, bk],
            [bk, bk, bk, bk, bk, cp, cp, cf, cf, cf, cf, cf, cf, cf, cf, cf, cf, cf, cp, cp, bk, bk, bk, bk, bk],
            [bk, bk, bk, bk, cp, cp, cf, cf, cf, cf, cf, cf, cf, cf, cf, cf, cf, cf, cf, cp, cp, bk, bk, bk, bk],
            [bk, bk, bk, bk, cp, cf, cf, cf, cf, cf, cf, cf, cf, cf, cf, cf, cf, cf, cf, cf, cp, cp, bk, bk, bk],
            [bk, bk, bk, cp, cf, cf, cf, cf, cf, cf, cf, cf, mk, cf, cf, cf, cf, cf, cf, cf, cf, cp, cp, cp, cp],
            [bk, bk, bk, cp, cf, cf, cf, cf, cf, mk, cf, mk, mk, mk, cf, mk, cf, cf, cf, cf, cf, cp, bk, bk, cp],
            [bk, bk, bk, cp, cf, cf, cf, cf, cf, mk, mk, mk, mk, mk, mk, mk, cf, cf, cf, cf, cf, cp, bk, bk, cp],
            [bk, bk, bk, cp, cf, cf, cf, cf, cf, cf, mk, mk, mk, mk, mk, cf, cf, cf, cf, cf, cf, cp, bk, bk, cp],
            [bk, bk, bk, cp, cf, cf, cf, cf, mk, mk, cf, mk, mk, mk, cf, mk, mk, cf, cf, cf, cf, cp, bk, bk, cp],
            [bk, bk, bk, cp, cf, cf, cf, cf, cf, mk, mk, mk, mk, mk, mk, mk, cf, cf, cf, cf, cf, cp, bk, bk, cp],
            [bk, bk, bk, cp, cf, cf, cf, mk, mk, cf, mk, mk, mk, mk, mk, cf, mk, mk, cf, cf, cf, cp, bk, bk, cp],
            [bk, bk, bk, cp, cf, cf, cf, cf, mk, mk, cf, mk, mk, mk, cf, mk, mk, cf, cf, cf, cf, cp, bk, bk, cp],
            [bk, bk, bk, cp, cf, cf, mk, mk, cf, mk, mk, mk, mk, mk, mk, mk, cf, mk, mk, cf, cf, cp, cp, cp, cp],
            [bk, bk, bk, cp, cp, cf, cf, mk, mk, cf, mk, mk, mk, mk, mk, cf, mk, mk, cf, cf, cp, cp, bk, bk, bk],
            [bk, bk, bk, cp, cp, cp, cf, cf, mk, mk, cf, mk, mk, mk, cf, mk, mk, cf, cf, cp, cp, cp, bk, bk, bk],
            [bk, bk, bk, cp, cp, cp, cp, cf, cf, mk, mk, mk, mk, mk, mk, mk, cf, cf, cp, cp, cp, cp, bk, bk, bk],
            [bk, bk, bk, cp, cp, cp, cp, cp, cf, cf, mk, mk, mk, mk, mk, cf, cf, cp, cp, cp, cp, cp, bk, bk, bk],
            [bk, bk, bk, cp, cp, cp, cp, cp, cp, cf, cf, mk, mk, mk, cf, cf, cp, cp, cp, cp, cp, cp, bk, bk, bk],
            [bk, bk, bk, cp, cp, cp, cp, cp, cp, cp, cf, cf, cf, cf, cf, cp, cp, cp, cp, cp, cp, cp, bk, bk, bk],
            [bk, bk, bk, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, bk, bk, bk],
            [bk, bk, bk, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, cp, bk, bk, bk],
        ]

        coffee_array = np.array(pixels_list_rosetta, dtype=np.uint8)
        coffee_image = Image.fromarray(coffee_array)
        coffee_image = coffee_image.resize((480, 480), resample=Image.NEAREST)
        coffee_image.save("coffee_rosetta.png")

        coffee_rosetta = Image.open("coffee_rosetta.png")
        coffee_rosetta.show()
        print("Thank you")
        break
    else:
        print("Sorry we can only do a heart or a rosetta")





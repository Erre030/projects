

#description: combine/paste images onto each other using the pillow library (PIL) and check certain constraints for the input to the program (number of arguments, file-extensions)

# use wget https://cs50.harvard.edu/python/2022/psets/6/shirt/shirt.png for shirt-image

import sys
from PIL import Image, ImageOps

def main():

    input, output = check_constraints()
    create_picture(input, output)






















def check_constraints():

    if len(sys.argv) != 3:
        sys.exit("Invalid number of arguments")

    input = sys.argv[1].lower()
    output = sys.argv[2].lower()

    #check file types
    if not input.endswith(".png") and not input.endswith(".jpg") and not input.endswith(".jpeg"):
        sys.exit("Invalid file type")

    if not output.endswith(".png") and not output.endswith(".jpg") and not output.endswith(".jpeg"):
        sys.exit("Invalid file type")

    _, type_input = input.rsplit('.',1)     #--> only splits one time at last point (from right side). _ means variable is not used afterwards/not important
    _, type_output = output.rsplit('.',1)

    if type_input != type_output:
        sys.exit("File extensions do not match")

    return input, output



def create_picture(in_file, out_file):

    with Image.open(in_file) as img, Image.open("shirt.png") as shirt:

        pic = ImageOps.fit(image= img, size= (600, 600))     #--> resize input picture, amount of pixels shown starting from middle
        pic_shirt = ImageOps.fit(image= shirt, size= (600,600))      #--> resize overlay picture (already has a transparent background)


        pic.paste(pic_shirt,(0,0),mask=pic_shirt)   #--> overlay pictures --> paste pic_shirt onto pic. mask is needed to activate "transparency of pic_shirt

        pic.save(out_file)  #--> save result with name of out_file


if __name__ == "__main__":
    main()

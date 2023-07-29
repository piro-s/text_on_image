import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def text_on_image(pos_x=10, pos_y=10, font_size=20, color_r=200, color_g=0, color_b=0):
    counter = 0 # for count processed images
    directory = os.getcwd() # assign directory

    # process all jpg in directory and susbfolders
    for filename in os.listdir(directory):
        filik = os.path.join(directory, filename)
        if os.path.isfile(filik): # if it's file
            file_type = filik.split('.')[-1].lower()
            if file_type == 'jpg' or file_type == 'png': # if it's jpg or png
                with Image.open(filik) as image:
                    image_filename = image.filename
                    if '_original' not in image_filename:
                        if '.png' in image_filename:
                            index = image_filename.find('.png')
                        elif '.jpg' in image_filename:
                            index = image_filename.find('.jpg')
                        
                        original = image_filename[:index] + '_original' + image_filename[index:]
                        if not os.path.isfile(original): # if file original do not exist, create backup and process image
                            image.save(original) # save backup

                            image_proc = ImageDraw.Draw(image)
                            # filik_name = filik.split('\\')[-1] # get filename without path      # Windows
                            filik_name = filik.split('/')[-1] # get filename without path         # Linux
                            myFont = ImageFont.truetype('FreeMono.ttf', font_size)
                            image_proc.text((pos_x, pos_y), filik_name, font=myFont, fill=(color_r, color_g, color_b))
                            image.save(filik)
                            image.close()

                            print(image_filename)
                            counter = counter + 1

    print("Number of processed images: " + str(counter) + '.')
    return


if __name__ == '__main__':
    text_on_image()
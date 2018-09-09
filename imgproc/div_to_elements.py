import cv2
import colorsys
import numpy as np
import os
from PIL import Image
import pytesseract

def extract_text(filename):

    # load the example image and convert it to grayscale
    image = cv2.imread(filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    

    # Image Pre Processing
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    #blur = cv2.medianBlur(gray, 3)

    threshFile = "{}.png".format(os.getpid())

    cv2.imwrite(threshFile, thresh)

    text = pytesseract.image_to_string(Image.open(threshFile))
    os.remove(threshFile)
    if text == '':
        return text, 'image'
    if text[0]=="#":
        command = text[0:2]
        text = text[3:]
        if command[1]=="L":
            textType= "link"
        elif command[1]=="P":
            textType="paragraph"
        elif command[1]=="H":
            textType="header"
        return text, textType
    else:
        return '', 'image'

def extract_elements(filename):

    # filename = "color_test.jpg"

    image = cv2.imread(filename)

    boundaries = [
        # [[0, 0, 120], [75, 75, 255]], # red
        # [[0, 0, 0], [255, 145, 75]], # green
        [[0, 0, 0], [255, 255, 255]] # black
    ]

    elements = {}

     # Threshholding
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    thresh = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)


    # loop over the boundaries
    for count, bounds in enumerate(boundaries):
        lower = bounds[0]
        upper = bounds[1]
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype = "uint8")
        upper = np.array(upper, dtype = "uint8")
     
        # find the colors within the specified boundaries and apply the mask
        mask = cv2.inRange(thresh, lower, upper)
        output = cv2.bitwise_and(thresh, thresh, mask = mask)

        # cv2.imshow('output', output)
        # cv2.waitKey(0)

        gray=cv2.cvtColor(output,cv2.COLOR_BGR2GRAY)
        edged = cv2.Canny(output, 10, 250)
        # cv2.imshow('edged', edged)
        # cv2.waitKey(0)

        _, cnts, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        x1,y1,w1,h1 = cv2.boundingRect(edged)
        width_bound = 0.15 * w1
        height_bound = 0.15 * h1

        idx = 0
        color = 'red_' if count == 1 else 'green_'
        for c in cnts:
            x,y,w,h = cv2.boundingRect(c)
            if (w>width_bound and h>height_bound):
                idx+=1
                new_img=image[y+25:y+h-25,x+25:x+w-25]
                imagefile = filename[:-4] + '_' + color + str(idx) + '.jpg'
                cv2.imwrite(imagefile, new_img)

                # top left corner of element relative to div class image picture
                text, element = extract_text(imagefile)
                elements[imagefile] = {'x-position': x, 'y-position': y, 'element': element, 'width': w, 'height': h, 'text': text}
            elif ((w > 3 * width_bound and h > 0.1 * h1) or (h > 3 * height_bound and w > 0.1 * w1)):
                idx+=1
                new_img=image[y+25:y+h-25,x+25:x+w-25]
                imagefile = filename[:-4] + '_' + color + str(idx) + '.jpg'
                cv2.imwrite(imagefile, new_img)

                # top left corner of element relative to div class image picture
                text, element = extract_text(imagefile)
                elements[imagefile] = {'x-position': x, 'y-position': y, 'element': element, 'width': w, 'height': h, 'text': text}

    return elements
    # output_file = '%s.json' % filename[:-4]

    # with open(output_file, 'w') as fp:
    #     json.dump(elements, fp, indent = 4)

# extract_elements('thresh_test_div_1_green_1.jpg')

import cv2
import os

def convert(filename):
    image = cv2.imread(filename)


    # Threshholding
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    #gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(image, 10, 250)
    # cv2.imshow('edged', edged)
    # cv2.waitKey(0)

    #finding_contours 
    
    #edged.copy() 
    _, cnts, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    x1,y1,w1,h1 = cv2.boundingRect(edged)
    width_bound = 0.7 * w1
    height_bound = 0.1 * h1

    divs = []
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        if w>width_bound and h>height_bound:
            new_img=image[y + 25:y+h-25,x+25:x+w-25]
            divs.append(new_img)
    
    divs.reverse()
    count = 0
    for new_img in divs:
        count += 1
        cv2.imwrite(filename[:-4] + '_div_' + str(count) + '.jpg', new_img)

    return count

# convert('thresh_test.jpg')
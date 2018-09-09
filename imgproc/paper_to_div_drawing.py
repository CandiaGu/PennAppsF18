import cv2
import os

def intersect(tl1, br1, tl2, br2):
    l1 = tl1[0]
    r1 = br1[0]
    t1 = tl1[1]
    b1 = br1[1]

    l2 = tl2[0]
    r2 = br2[0]
    t2 = tl2[1]
    b2 = br2[1]

    if l1 > r2 or r1 < l2 or t1 > b2 or b1 < t2:
        return False
    return True

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
        x += 25
        y += 25
        h -= 25
        w -= 25

        good = True
        for div in divs:
            img_x, img_y, img_w, img_h = div[1]
            if intersect((x,y), (x+w,y+h), (img_x,img_y), (img_x+img_w,img_y+img_h)):
                good = False
                break

        if good and w>width_bound and h>height_bound:
            new_img=image[y:y+h,x:x+w]
            divs.append((new_img, (x, y, w, h)))
    
    divs = [ t[0] for t in divs ]
    divs.reverse()
    count = 0
    for new_img in divs:
        count += 1
        cv2.imwrite(filename[:-4] + '_div_' + str(count) + '.jpg', new_img)

    return count

# convert('thresh_test.jpg')
import cv2

def convert(filename):
    image = cv2.imread(filename)
    #gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(image, 10, 250)

    # cv2.imshow('edged', edged)
    # cv2.waitKey(0)

    #finding_contours 
    
    #edged.copy() 
    _, cnts, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    x1,y1,w1,h1 = cv2.boundingRect(edged)
    width_bound = 0.9 * w1
    height_bound = 0.05 * h1

    divs = []
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        if w>width_bound and h>height_bound:
            new_img=image[y:y+h,x:x+w]
            divs.append(new_img)
    
    divs.reverse()
    count = 0
    for new_img in divs:
        count += 1
        cv2.imwrite(filename[:-4] + ' _' + str(count) + '.jpg', new_img)

    return count

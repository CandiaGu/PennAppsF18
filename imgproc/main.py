import paper_to_div, paper_to_div_drawing
import div_to_elements, div_to_elements_drawing
import json

drawing = '0.jpg'

def main():
    filename = 'test2.jpg'
    filename_drawing = drawing

    convertImgtoInfo(filename_drawing)

def convertImgtoInfo(filename):

    if filename == 'test2.jpg':
        num_divs = paper_to_div.convert(filename)
    elif filename == drawing:
        num_divs = paper_to_div_drawing.convert(filename)

    divs = {}

    #If there are no divs detected then we will assume that the paper is blank so we will not update it
    if(num_divs)==0:
        return 0
    
    for i in range(num_divs):
        div = filename[:-4] + '_div_%d' % (i + 1) + '.jpg'
        if filename == 'test2.jpg':
            div_elements, div_height, div_width = div_to_elements.extract_elements(div)
        elif filename == drawing:
            div_elements, div_height, div_width = div_to_elements_drawing.extract_elements(div)
        divs[div] = {'height': div_height, 'width': div_width, 'elements': div_elements}

    print json.dumps(divs, sort_keys=True, indent=4)
    return divs

main()

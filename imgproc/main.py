import paper_to_div
import div_to_elements
import json

def main():
    filename = 'test2.jpg'

    convertImgtoInfo(filename)

def convertImgtoInfo(filename):

    num_divs = paper_to_div.convert(filename)

    divs = {}

    #If there are no divs detected then we will assume that the paper is blank so we will not update it
    if(num_divs)==0:
        return 0
    
    for i in range(num_divs):
        div = filename[:-4] + '_div_%d' % (i + 1) + '.jpg'
        div_elements, div_height, div_width = div_to_elements.extract_elements(div)
        divs[div] = {'height': div_height, 'width': div_width, 'elements': div_elements}

    print json.dumps(divs, sort_keys=True, indent=4)
    return divs

main()

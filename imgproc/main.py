import paper_to_div
import div_to_elements

def main():
    filename = 'test_2.jpg'

    num_divs = paper_to_div.convert(filename)

    divs = []

    #If there are no divs detected then we will assume that the paper is blank so we will not update it
    if(num_divs)==0:
        return 0
    
    for i in range(num_divs):
        div = filename[:-4] + '_%d' % (i + 1) + '.jpg'
        # div = 'color_test.jpg'
        div_to_elements.extract_elements(div)
        divs.append(div[:-4] + '.json')



main()
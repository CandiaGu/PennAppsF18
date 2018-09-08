import paper_to_div
import div_to_elements

def main():
    filename = '/Users/michaelkronovet/Desktop/fart2.jpg'

    num_divs = paper_to_div.convert(filename)

    divs = []

    #If there are no divs detected then we will assume that the paper is blank so we will not update it
    if(num_divs)==0:
        return 0
    
    for i in range(num_divs):
        div = filename[:-4] + '_%d' + str(i + 1) + '.jpg'
        div_to_elements.extract_elements(div)
        divs.append(div[:-4] + '.json')



main()
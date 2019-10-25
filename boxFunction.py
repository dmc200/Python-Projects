"""

Example Output:
***********
*         *
*         *
***********

"""


def boxPrint(symbol, width, height):
    if len(symbol) != 1:
            raise Exception('Symbol needs to be a string of length 1.')
    if (width < 2) or (height < 2):
            raise Exception('Width or Height need to be greater than 1.')
    print(symbol * width)
    for i in range(height-2):
        print(symbol + (' ' * (width-2)) + symbol)
    print(symbol * width)
    
    

    
boxPrint('*', 1, 1)

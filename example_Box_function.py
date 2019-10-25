


def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string of length 1')
    if width <= 1 or height <= 1:
        raise Exception('"width" and or "height" need to be larger than 1')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)


boxPrint('*', 15, 1)


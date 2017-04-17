
def convert(x, string):

    # creates a dictionary full of hex remainders
    remainders = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A',
                  11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    
    r = x % 16
    q = int(x / 16)
    
    hex_string = remainders[r] + string

    if x >= 16:
        hex_string = convert(q, hex_string)  # if x is greater than 16, recurse using x / 16
        return hex_string

    else:
        print(hex_string)
        return hex_string


def convert_dec_to_hex(x):

    hex = convert(x, "")
    return hex


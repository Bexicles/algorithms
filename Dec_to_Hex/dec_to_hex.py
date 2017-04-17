
ans = ""    # creates an empty string in which to store string answer


def convert_dec_to_hex(x):
    # creates a dictionary full of hex remainders
    remainders = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A',
                  11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    
    r = x % 16
    d = x / 16
    
    global ans
    ans = remainders[r] + ans
    
    if x > 16:
        convert_dec_to_hex(int(d))  # if x is greater than 16, recurse using x / 16
    
    else:
        print(ans)

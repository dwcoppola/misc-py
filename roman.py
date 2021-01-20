import math

def int_to_roman(num):
    try:
        if int(num) > 3999 or int(num) < 1:
            return "Value Error"
        else:
            ones = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"] 
            tens = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
            hundreds = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
            thousands = ["M", "MM", "MMM"]
            new_arr = []
            place_count = 1
            for v in str(num)[::-1]:
                if int(v) == 0:
                    place_count += 1
                    continue
                else:
                    if place_count == 1:
                        new_arr.append(ones[int(v) - 1])
                    elif place_count == 2:
                        new_arr.append(tens[int(v) - 1])
                    elif place_count == 3:
                        new_arr.append(hundreds[int(v) - 1])
                    else:
                        new_arr.append(thousands[int(v) - 1])
                place_count += 1
        return "".join(new_arr[::-1])
    except:
        return "Value Error"
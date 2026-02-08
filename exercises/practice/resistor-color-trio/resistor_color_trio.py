
dict = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }
    

def get_color1_index(color1): 
    if color1 in dict:
        for c in dict:
            s = dict[color1]
        return s
    else:
        return "The color doesn't exist."

def get_color2_index(color2): 
    if color2 in dict:
        for c in dict:
            s = dict[color2]
        return s
    else:
        return "The color doesn't exist."
        
def value(colors):
    color1 = colors[0]
    color2 = colors[1]
    color3 = colors[2]
    
    ind1 = str(get_color1_index(color1))
    ind2 = str(get_color2_index(color2))
    ind  = ind1 + ind2 + 
    value = int(ind)
    return value

print(value(["brown", "black"]))
print(value(["brown", "black"]) == 10)

import numpy as np
import binascii

def the_humourless_route(data):
    return np.frombuffer(data, dtype=np.uint8).reshape(240, 424, 3)

def the_scenic_route(data):
    #....Some TCP stuff before, and this code is in a loop:
    #Convert from hex binary to string
    asstr = binascii.hexlify(data)
    #Split up after each byte couple
    n = 2
    split = [asstr[i:i+n] for i in range(0, len(asstr), n)]
    #Convert each byte couple to integer from its hex representation    
    asint = [];
    for i in split:    
        asint.append(int(i,16))   

    #Reshape into red,green and blue
    try:
        red = np.asarray(asint[::3]).reshape(240, 424) 
        green = np.asarray(asint[1::3]).reshape(240,424)
        blue = np.asarray(asint[2::3]).reshape(240,424)
    except ValueError:
        pass

    #Reshape into an Image representation for opencv
    img = np.transpose(np.asarray([red,green,blue],dtype=np.uint8),axes=(1, 2, 0)) # pyright: reportUnboundVariable=false
    return img

data = bytes(np.random.randint(0, 256, (240*424*3,)).tolist())
print(np.all(the_scenic_route(data) == the_humourless_route(data)))
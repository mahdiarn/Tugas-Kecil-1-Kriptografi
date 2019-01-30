import random

def generateAutoKey(input,key):
    if (len(key) == len(input)):
        return key
    elif (len(key) > len(input)):
        output = ""
        idx = 0
        while (len(output) != len(input)):
            output = output + key[idx]
            idx += 1
        return output
    else:
        output = key
        idx = 0
        while (len(output) != len(input)):
            output = output + input[idx]
            idx += 1
        return output

print(generateAutoKey("mahdiarnaufal","bibubi"))
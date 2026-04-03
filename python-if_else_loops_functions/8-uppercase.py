#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # Herfin kiÃ§ik olub-olmadgÄ±±nÄ± yoxlayÄ
        temp_char = char
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            temp_char = chr(ord(char) - 32)
        print("{}".format(temp_char), end="")
    print("")

import numpy as np
from functools import reduce

def decipher(cipher, key):
    key = (ord(key[0]), ord(key[1]), ord(key[2]))
    decipher = ""
    for i,c in enumerate(cipher):
        decipher += chr(cipher[i] ^ key[i%3])
    return decipher

if __name__ == "__main__":
    cipher = np.loadtxt("p059_cipher.txt", delimiter=",", dtype=int)

    for c1 in range(97,122+1):
        for c2 in range(97,122+1):
            for c3 in range(97,122+1):
                key = chr(c1) + chr(c2) + chr(c3)
                text = decipher(cipher, key)
                if "the" in text and "of" in text and "to" in text and "and" in text and text.count(" ") > 100:
                    s = sum(map(ord, text))
                    
                    print(key, s)
                    print(text)
                    input()

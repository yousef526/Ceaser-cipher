from .CeaserClass import Ceaser


def get_cipher(string,  encrypt=True,key=None):
    string = string.lower()
    key_ = {"a": "d", "b": "e", "c": "f", "d": "g", "e": "h", "f": "i", "g": "j",
            "h": "k","i": "l", "j": "m", "k": "n", "l": "o", "m": "p", "n": "q", "o":
            "r", "p": "s","q": "t", "r": "u", "s": "v", "t": "w", "u": "x", "v": "y",
            "w": "z", "x": "a","y": "b", "z": "c", " ":" "}

    
    if key is None:
        key = key_
        del key_
    else:
        del key_
    antiKey = {key[x]:x for x in key}
    
    c = Ceaser(key=key, antiKey=antiKey)

    return c.process_str(string,encrypt)

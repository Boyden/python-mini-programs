import base64

def safe_b64decode(s):
    while len(s) % 4 != 0:
        s += '='
    return base64.b64decode(s)
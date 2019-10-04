import base64

def weirdEncoding(encoding, message):
    return base64.b64decode(s=message, altchars=encoding).decode()

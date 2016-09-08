import os

#TODO expand these dictionaries with more constants
ASCII = {
    'NEW_LINE':     os.linesep.encode('ascii'),
    'BACKSPACE':    '08'.encode('ascii'),
    'DELETE':       '127'.encode('ascii')
}

IAC = {
    'IAC': 255
}

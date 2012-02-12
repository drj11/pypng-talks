import png
import urllib

def apng(short='basn0g01'):
    if 'png' not in short:
       short += '.png'
    prefix = "http://www.schaik.com/pngsuite/"
    return urllib.urlopen(prefix + short)

import png
import urllib

f = urllib.urlopen("http://www.schaik.com/pngsuite/basn0g01.png")
r = png.Reader(file=f)
x,y,pixels,info = r.read()
for row in pixels:
    print row

x,y,pixels,info = png.Reader(
  file=urllib.urlopen("http://www.schaik.com/pngsuite/basn0g01.png")).read()
for row in pixels:
    print ''.join(str(p) for p in row)

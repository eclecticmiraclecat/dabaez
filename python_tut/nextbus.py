# nextbus.py

import sys

if len(sys.argv) != 3:
    raise SystemExit('Usage: nextbus.py route stopid')

route = sys.argv[1]
stopid = sys.argv[2]

import urllib.request

u = urllib.request.urlopen(f'http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop={stopid}&route={route}')
data = u.read()

from xml.etree.ElementTree import XML
doc = XML(data)

import pdb; pdb.set_trace()     # Launch debugger

for pt in doc.findall('.//pt'):
    print(pt.txt)

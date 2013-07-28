#!/usr/bin/env python
"""
Simple script example of data processing and plotting
using pylab (matplotlib).
"""

# NOTE: you may need to put the following line in ~/.matplotlib/matplotlibrc 
"""
backend: TkAgg
"""

from pylab import *

data = """
Amsterdam   52.8    9.0     2.5e6   18.2
Berlin      52.5    13.3    4.0e6   18.9
Brussels    50.5    7.5     2.6e6   18.9
Lisbon      38.7    -9.2    2.6e6   21.4
London      52.1    0.0     1.3e7   17.3
Madrid      40.4    -3.7    5.3e6   21.2
Paris       48.7    2.3     1.1e7   19.7
Rome        41.9    12.5    3.1e6   23.4
Vienna      47.9    16.8    2.6e6   18.5
Zurich      50.0    9.5     1.6e6   17.8
"""

SCALING_FACTOR = 2e3
SMALL_CITY     = 3.5e5

figure()

for entry in data.splitlines():
    parts = entry.split()
    if len(parts) < 5:
        continue

    city  = parts[0]
    lat   = float(parts[1])
    lon   = float(parts[2])
    pop   = float(parts[3])
    temp  = float(parts[4])

    if pop < SMALL_CITY: # skip small cities
        continue

    scatter(lon, lat, s=pop/SCALING_FACTOR, c=temp,
            vmin=17.0, vmax=24.0, cmap=hot(), alpha=0.3)
    text(lon, lat, city)

title("Population and May max temperatures\n" +
		"of major European metropolitan areas")
xlabel("longitude")
ylabel("latitude")
colorbar()
show()

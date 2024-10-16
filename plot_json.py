#!/usr/bin/env python

import matplotlib.pyplot as plt
import json
import sys
import argparse
import os


parser = argparse.ArgumentParser(description='memapper plot program')

# Profile Support
parser.add_argument('-i', '--input', required=True, type=str, help="Input JSON file to plot")
parser.add_argument('-o', '--out', type=str, help="Output file")


args = parser.parse_args(sys.argv[1:])

with open(args.input, "r") as f:
    data = json.load(f)

axes = range(0, len(data.keys()))

z = []
for k in data.keys():
    loc = []
    for kk in data.keys():
        v = data[k][kk]
        loc.append(v)
    z.append(loc)

fig, ax = plt.subplots()
   
c = ax.pcolormesh(axes, axes, z, shading='auto')

fig.colorbar(c, ax = ax)

machine=os.popen("cat /proc/cpuinfo | awk '/model name/{print $0 ; exit}' | cut -d \":\" -f 2").readline()
plt.title(machine)

if args.out:
    plt.savefig(args.out)
else:
    plt.show()


#!/usr/bin/env python

import os, sys

usage_string = 'usage: txt2csv.py {tr|te} input output'

if len(sys.argv) != 4:
    print(usage_string)
    exit(1)

type, src_path, dst_path = sys.argv[1:]

if type == 'tr':
    header = 'Label,I1,I2,I3,C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13,C14,C15,C16'
    idx = 10000000
elif type == 'te':
    header = 'I1,I2,I3,C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13,C14,C15,C16'
    idx = 60000000
else:
    print(usage_string)
    exit(1)

with open(dst_path, 'w') as f:
    f.write(header + '\r\n')
    for line in open(src_path, 'r'):
        line = str(idx) + ',' + line.replace('\t', ',')
        f.write(line.replace('\n', '\r\n'))
        idx += 1

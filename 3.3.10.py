import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.match(r".*\\.*", line):
        print(line)
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.match(r".*z.{3}z.*", line):
        print(line)
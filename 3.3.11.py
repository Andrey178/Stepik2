import sys
import re

for line in sys.stdin:
    line = line.rstrip()

    for _ in line.split():
        if re.match(r"\b(.+?)\1\b", _):
            print(line)
            break
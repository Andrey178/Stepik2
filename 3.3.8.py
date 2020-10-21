import sys
import re

for line in sys.stdin:
    line = line.rstrip()
#    print(f'GOT: {line}')
    if re.match(r".*\bcat\b.*", line):
        print(line)
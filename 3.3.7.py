import sys
import re

for line in sys.stdin:
    line = line.rstrip()
#    print(f'GOT: {line}')
    lst = re.match(r".*cat.*cat.*", line)
#    print(f'FOUND: {lst}')
#    if len(lst) > 1:
#        print(line)
    try:
        print(lst.group())
    except AttributeError:
        pass

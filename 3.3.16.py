import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    result = re.search(r"[01]+", line)
    if not result:
        break
    even, noteven = 0, 0
    for ind, itm in enumerate(line):
        if re.match(r"1", itm):
            if ind % 2 == 0:
                even += 1
            else:
                noteven += 1
    if (noteven - even) % 3 == 0:
        print(line)

    if re.match(r"^(0|(1(01*0)*1))*$", line):
        print(f"got: {line}")
    if re.fullmatch(r"(0|(1(01*0)*1))*", line):
        print(f"got: {line}")



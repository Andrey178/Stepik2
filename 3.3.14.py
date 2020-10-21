import sys
import re

for line in sys.stdin:
    pattern = re.compile(r"\b(\w)(\w)(\w*)\b")
    pattern2 = r"\b(\w)(\w)"
    print(pattern.sub(r"\2\1\3", line.rstrip()))
    print(re.sub(pattern2, r"\2\1", line.rstrip()))
#    print(pattern.subn("computer", line))


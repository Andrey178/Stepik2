import sys
import re

for line in sys.stdin:
    pattern = re.compile(r"human")
    print(pattern.sub("computer", line.rstrip()))
    print(pattern.subn("computer", line))
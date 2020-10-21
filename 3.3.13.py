import sys
import re

for line in sys.stdin:
    pattern = re.compile(r"\ba+\b", re.IGNORECASE)
    print(pattern.sub("argh", line.rstrip(), 1))
#    print(pattern.subn("computer", line))

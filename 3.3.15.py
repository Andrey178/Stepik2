import sys
import re

for line in sys.stdin:
    pattern = re.compile(r"(\w)\1*", flags=re.UNICODE | re.IGNORECASE)
    pattern2 = r"\b(\w)(\w)"
    print(pattern.subn(r"\1", line.rstrip()))
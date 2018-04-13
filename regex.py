import sys
import re
print(bool(re.match(".*"+sys.argv[1]+".*", sys.argv[2], re.IGNORECASE)))
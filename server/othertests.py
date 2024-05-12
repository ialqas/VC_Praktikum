import sys
import os

print(sys.prefix != sys.base_prefix)
print(sys.prefix)
print(sys.base_prefix)

#print("checking os approach")
#print(os.environ["VIRTUAL_ENV"])
import sys
import ctypes
import struct

print(sys.version, sys.platform)

a = 5
b = 125.54
c = 'Hello world!'

print(id(a))
print(sys.getsizeof(a))

print(ctypes.string_at(id(a), sys.getsizeof(a)))

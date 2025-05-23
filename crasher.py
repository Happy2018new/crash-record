import ctypes
import time

LIB1 = ctypes.cdll.LoadLibrary("./c1.so")
LIB2 = ctypes.cdll.LoadLibrary("./c2.so")


LIB1.DO.argtypes = []
LIB1.DO.restype = None
LIB2.DO.argtypes = []
LIB2.DO.restype = None

LIB1.DO()
LIB2.DO()
time.sleep(1)
print("OK")

import talib
import numpy
close = numpy.random.random(100)
print(type(close))
print(close)
output = talib.SMA(close)
print(output)
# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
import numpy
#import scipy

N = get_number()
cb = get_number()
cp = get_number()

x = []
y = []

for i in range(N):
     x1 = get_number()
     y1 = get_number()
     x.append(x1)
     y.append(y1)
x_total = sum(x)
y_total = sum(y)
xt = numpy.ceil(x_total/10) #approximate upto to next int
yt = numpy.ceil(y_total/10) #approximate upto to next int
cost_b = xt* cb #need the approxed number
cost_p = yt * cp
print(int(cost_b+cost_p))
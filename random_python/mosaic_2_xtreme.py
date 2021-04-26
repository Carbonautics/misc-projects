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
cut_h = 0
cut_v = 0
number_tiles = 1
w = get_number()
h= get_number()
a = get_number()
b = get_number()
m = get_number()
c = get_number()
if(a > 0 and w >= a and w % a > 0):
    number_tiles *= int(numpy.ceil(w/a))
elif(a > 0 and w >= a):
    number_tiles *= int(w/a)

if(b > 0 and h>=b and h % b > 0):
    number_tiles *= int(numpy.ceil(h/b))
    if(a > 1):
        cut_h = (w + h)
        if(a==b):
            cut_h = w
    else:
        cut_h = w
    cut_v = 0
elif(b > 0 and h >= b):
    number_tiles *= int(h/b)
    cut_h = 0
    if(h==b):
        if(a > 1):
            cut_v = h
    else:
        if(a > 1):
            cut_v = h
        else:
            cut_v = 0
            cut_h = w
if((a == 1 and a == b) or (w == a and h==b)): #or ((w*h) == (a*b))):
    cut_h = 0
    cut_v = 0
cost_tiles = (int(numpy.ceil(number_tiles/10)) * m) + (cut_v * c) + (cut_h * c)
print(cost_tiles)
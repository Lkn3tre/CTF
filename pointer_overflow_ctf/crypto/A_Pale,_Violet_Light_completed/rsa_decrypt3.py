from Cryptodome.Util.number import *

## the gcdExtended function is copied from GeeksforGeeeks and u must at least know that it exists.

def gcdExtended(a, b):

    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcdExtended(b % a, a)


    x = y1 - (b//a) * x1
    y = x1

    return gcd ,x ,y

def get_d(phi,e):
    number=gcdExtended(phi,e)[2]
    if number<0:
        return number +phi
    else:
        return number

e=5039
n=34034827
c="933969 15848125 24252056 5387227 5511551 10881790 3267174 14500698 28242580 933969 32093017 18035208 2594090 2594090 9122397 21290815 15930721 4502231 5173234 21290815 23241728 2594090 21290815 18035208 10891227 15930721 202434 202434 21290815 5511551 202434 4502231 5173234 25243036".split(' ')

phi=(5861-1)*(5807-1) # You can find p and q in factordb.com
d=get_d(phi,e)                                                                              # or in termainal by using factordb
for i in c :
	m=pow(int(i),d,n)
	print(long_to_bytes(m).decode('ascii'),end='')

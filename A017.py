import numpy as np
import operator
import re

numbers = {1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
numbers.update({10:"Ten",20:"Twenty",30:"Thirty",40:"Forty",50:"Fivty",60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety"})
numbers.update({11:"Eleven",12:"Twelve",13:"Thriteen",14:"Fourteen",15:"Fivteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen"})

for k in xrange(1,1001):
    if not k in numbers:
        if k < 100:
            numbers[k]= '{}-{}'.format(numbers[int(k*.1)*10],numbers[k%10])
        elif k % 1000 == 0:
            numbers[k] = '{} thousand'.format(numbers[int(k*.001)])
        elif k % 100 == 0:
            numbers[k] = '{} hundred'.format(numbers[int(k*.01)])
        else:
            numbers[k] = '{} and {}'.format(numbers[int(k*.01)*100],numbers[int(str(k)[1:3])])

print('The number of characters in this sequence is {}'.format(sum(len(re.sub('[ -]','',k)) for k in numbers.values())))
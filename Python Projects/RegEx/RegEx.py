# This program will extract all the number in this document, and compute a sum at the end.
# I use regular expressions, "for" loops, and conditionals to accomplish this.
import re
hand = open("regex_sum_265510.txt")
accum = list()
accum2 = list()
sigma = 0
for line in hand :
    line.strip()
    line = re.findall('[0-9]+', line)
    accum.append(line)

# This loop has the purpose of considering list of 1, 2, and 3 indexes.
# Also add them to another list.
for itr in accum :
    if len(itr)==1 :
        accum2.append(itr[0])
    if len(itr)==2 :
        accum2.append(itr[0])
        accum2.append(itr[1])
    if len(itr)==3 :
        accum2.append(itr[0])
        accum2.append(itr[1])
        accum2.append(itr[2])

# I Iterate within the list elements to achieve the sum.
# The reason why I created two different lists is because we need to filter the values and
# use just the ones actually containing a value.
for number in accum2 :
    sigma = sigma + int(number)

# The variable sigma will store the addition of the "accum2" items.
# The output should be 563135
print(sigma)


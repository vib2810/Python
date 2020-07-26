from collections import Counter
import re
import sys

if sys.version_info <(2,7):
    Sys.exit("Must use Python 2.7 or greater")

if len(sys.argv)<2:
    sys.exit('Usage: python %s filename N'%sys.argv[0])

n=0
if len(sys.argv)>2:
    try:
        n=int(sys.argv[2])
        if n<=0:
            raise ValueError
    except ValueError:
        sys.exit("Invalid value for N: %s.\nN must be an integer greater than 0"%sys.argv[2])

filename=sys.argv[1]
try:
        with open(filename,"r") as input_text:
            wordcounter=Counter()
            for line in input_text:
                 wordcounter.update(re.findall("\w+",line.lower()))
        if n==0:
            n=len(wordcounter)

        for word, frequency in wordcounter.most_common(n):
            print("%s %d" % (word, frequency))

except IOError:
        sys.exit("Cannot open file: %s"% filename)
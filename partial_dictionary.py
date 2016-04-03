import re, collections
def words(text): return re.findall('[a-z]+', text.lower())
#http://norvig.com/big.txt
myList = words(file('big.txt').read())
print(len(myList));


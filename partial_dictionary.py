import re, collections
import urllib2
import sys

def words(text): 
   return re.findall('[a-z]+', text.lower());


if len(sys.argv) == 1: 
   print("usage: %s http://norvig.com/big.txt" % (sys.argv[0]));
   sys.exit(0);

myurl = (str(sys.argv[1]))

hdr = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
request = urllib2.Request(myurl, headers=hdr);
result = urllib2.urlopen(request);
the_page = result.read();

dupList = words(the_page);
noDupList=list(set(dupList));
sortedNoDupList = sorted(noDupList);

for x in sortedNoDupList:
   print("%s" % (x)) 


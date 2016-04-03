import re, collections
import urllib2

def words(text): return re.findall('[a-z]+', text.lower());

myurl = 'http://norvig.com/big.txt';
hdr = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
request = urllib2.Request(myurl, headers=hdr);
result = urllib2.urlopen(request);
the_page = result.read();




dupList = words(the_page);
noDupList=list(set(dupList));
sortedNoDupList = sorted(noDupList);
print(sortedNoDupList);


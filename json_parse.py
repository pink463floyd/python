import json
import urllib2
import sys
from pprint import pprint


myurl = (str(sys.argv[1]))
print (myurl);

data = json.load(urllib2.urlopen(myurl));
pprint(data)





import json
import urllib2
import urllib2, base64
from pprint import pprint


myurl = 'https://parking.api.smgov.net/lots'
username = 'scottl@civicresource.com';
password = 'foobar!';

request = urllib2.Request(myurl)
base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string)   
result = urllib2.urlopen(request)
the_page = result.read()


pprint(the_page);

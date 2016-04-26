import json
import urllib2
import urllib2, base64
from pprint import pprint


stopurl = 'http://api.metro.net/agencies/lametro/routes/%s/stops'
myurl = 'http://api.metro.net/agencies/lametro/routes/'

request = urllib2.Request(myurl)
result = urllib2.urlopen(request)
data = json.load(result);
myLen = len(data['items']);
i = 0;
visited=set();
while i<myLen:
   #print(data['items'][i]);
   #print(data['items'][i]['display_name']);
   id = data['items'][i]['id'];
   i = i+1;
   
   stopurl = 'http://api.metro.net/agencies/lametro/routes/%s/stops' % (id);
   #print(stopurl);
   request2 = urllib2.Request(stopurl)
   result2 = urllib2.urlopen(request2)
   data2 = json.load(result2);
   myLen2 = len(data2['items']);
   j=0;
   while j<myLen2:
      if 'id' not in data2['items'][j]:
         print("**********************Route %s has a missing id element" % (id));
         print(data2['items'][j]['display_name']);
      j=j+1;

import json
import time
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
print("id, display_name, longitude, lattude");
while i<myLen:
   id = data['items'][i]['id'];
   i = i+1;
   
   stopurl = 'http://api.metro.net/agencies/lametro/routes/%s/stops' % (id);
   print(stopurl);
   request2 = urllib2.Request(stopurl)
   result2 = urllib2.urlopen(request2)
   data2 = json.load(result2);
   myLen2 = len(data2['items']);
   j=0;
   while j<myLen2:
      if 'id' not in data2['items'][j]:
         print("**********************Route %s has a missing id element" % (id));
         break;
      else:
         #print(data2['items'][j]['id']);
         stop_id = data2['items'][j]['id'];
         if stop_id in visited:
           print("**********************dup stop: ", stop_id);
           break;
         else: 
           visited.add(stop_id);
           print("%s,%s,%f,%f" % (
                 data2['items'][j]['id'],
                 data2['items'][j]['display_name'],
                 data2['items'][j]['latitude'],
                 data2['items'][j]['longitude']));
      j = j+1;
      time.sleep(.3);

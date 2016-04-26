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
   print stopurl;
   request2 = urllib2.Request(stopurl)
   result2 = urllib2.urlopen(request2)
   data2 = json.load(result2);
   myLen2 = len(data2['items']);
   j=0;
   while j<myLen2:
      print(data2['items'][j]['display_name']);
      if 'id' not in data2['items'][j]:
         print("**********************Route %s has a missing id element" % (id));
      else:
         stop_id = data2['items'][j]['id'];
         if stop_id in visited:
           print("**********************dup stop: ", stop_id);
         else: 
           visited.add(stop_id);
           print(data2['items'][j]['id']);
           predurl = 'http://api.metro.net/agencies/lametro/stops/%s/predictions' % (stop_id);
           print(predurl);
           request3 = urllib2.Request(predurl)
           result3 = urllib2.urlopen(request3)
           data3 = json.load(result3);
           myLen3 = len(data3['items']);
           k=0;
           while k<myLen3:
             print(data3['items'][k]['route_id'], data3['items'][k]['seconds']);
             k=k+1;
      j = j+1;






#print(data);
#pprint(data);

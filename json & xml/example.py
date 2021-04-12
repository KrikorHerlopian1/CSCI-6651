import json
from urllib.request import urlopen
from urllib.parse import urlencode
import xml.etree.ElementTree as ET


dic = {'zip':'06510', 'location':'New Haven', 'appid':'594e5f233a85c3d9edb027496e0518ee'}
encoding= urlencode(dic)
url = "http://api.openweathermap.org/data/2.5/weather?"+encoding
req = urlopen(url)
data = json.load(req)
if "weather" in data:
	a = len(data["weather"])
	x = 0	
	while x < a:
		print("weather description", data["weather"][x]["description"])
		x = x+1



tree = ET.parse('sample.xml')
root = tree.getroot()
print("root tag from xml file " , root.tag)

data_as_string = '<data><country name="Liechtenstein"><rank>1</rank><year>2008</year><gdppc>141100</gdppc><neighbor name="Austria" direction="E"/><neighbor name="Switzerland" direction="W"/> </country><country name="Singapore"><rank>4</rank><year>2011</year><gdppc>59900</gdppc><neighbor name="Malaysia" direction="N"/> </country><country name="Panama"><rank>68</rank><year>2011</year> <gdppc>13600</gdppc><neighbor name="Costa Rica" direction="W"/><neighbor name="Colombia" direction="E"/></country></data>'
root = ET.fromstring(data_as_string)
print("root tag from xml string " ,root.tag)




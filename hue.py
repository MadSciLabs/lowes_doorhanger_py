import requests
import json

TAG_1 = "3720938632"
TAG_2 = "3709076616"
TAG_3 = "3702850696"

r = requests.get("http://192.168.1.106/api/newdeveloper")

light_vals = []

light_vals.append([])
light_vals.append([])
light_vals.append([])

light_vals[0].append({"sat": 208, "bri": 207, "hue": 13234})
light_vals[0].append({"sat": 253, "bri": 230, "hue": 65527})
light_vals[0].append({"sat": 208, "bri": 207, "hue": 13234})

light_vals[1].append({"sat": 232, "bri": 203, "hue": 34495})
light_vals[1].append({"sat": 232, "bri": 203, "hue": 34495})
light_vals[1].append({"sat": 232, "bri": 203, "hue": 34495})

light_vals[2].append({"sat": 0, "bri": 0, "hue": 0})
light_vals[2].append({"sat": 0, "bri": 0, "hue": 0})
light_vals[2].append({"sat": 0, "bri": 0, "hue": 0})

#print(r.status_code)
#print(r.content)
#_url = "http://192.168.1.106/api/newdeveloper/lights/2/state"

setIndex = 0

def setLights(_setIndex):

  for i in range(0, 3):

    _url = "http://192.168.1.106/api/newdeveloper/lights/" + str(i+1) + "/state"
    _payload = json.dumps(light_vals[_setIndex][i])

    print(_url)
    print(_payload)

    r = requests.put(_url, _payload)

    print(r.status_code)
    print(r.content)


while (True):
  _rfid = input("rfid:");
  print(_rfid);

  if str(_rfid) == TAG_1:

    setLights(0);

  if str(_rfid) == TAG_2:

    setLights(1);

  if str(_rfid) == TAG_3:

    setLights(2);


import requests
getdata = requests.get("http://api.open-notify.org/iss-now.json")
getjsondata = getdata.json()

lati = getjsondata["iss_position"]["latitude"]
longi = getjsondata["iss_position"]["longitude"]
print("CURRENT LOCATION OF THE ISS:")
print("Lon: {longi}  Lat: {lati}")
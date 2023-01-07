# Import Modules
from xml.dom import minidom
from urllib.request import urlopen

openedUrl = urlopen("http://assignments.reaktor.com/birdnest/drones")
document = minidom.parse(openedUrl)
print(document)
drones = document.getElementsByTagName("drone")
for drone in drones:
	serialNumber = drone.getElementsByTagName("serialNumber")[0]
	print(serialNumber.firstChild.data)
	posY = drone.getElementsByTagName("positionY")[0]
	print(posY.firstChild.data)
	posX = drone.getElementsByTagName("positionX")[0]
	print(posX.firstChild.data)
	print("\n")
